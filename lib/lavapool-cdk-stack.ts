import {Construct} from 'constructs';
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apigateway from 'aws-cdk-lib/aws-apigatewayv2';
import * as integrations from 'aws-cdk-lib/aws-apigatewayv2-integrations';
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as secretsmanager from "aws-cdk-lib/aws-secretsmanager";
import * as rds from "aws-cdk-lib/aws-rds";

export class LavapoolCdkStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        const vpc = new ec2.Vpc(this, 'Lavapool-VPC', {
            maxAzs: 2,
        });

        const dbSecret = new secretsmanager.Secret(this, 'Lavapool-DbSecrets', {
            generateSecretString: {
                secretStringTemplate: JSON.stringify({
                    username: 'lavapool'
                }),
                excludePunctuation: true,
                includeSpace: false,
                generateStringKey: 'password',
            },
        });

        const dbSecurityGroup = new ec2.SecurityGroup(this, 'Lavapool-DbSecurityGroup', {
            vpc,
            allowAllOutbound: true,
        });
        dbSecurityGroup.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(5432), 'Allow PostgreSQL access');

        const auroraCluster = new rds.ServerlessCluster(this, 'Lavapool-AuroraPostgresCluster', {
            engine: rds.DatabaseClusterEngine.auroraPostgres({
                version: rds.AuroraPostgresEngineVersion.VER_13_6,
            }),
            vpc,
            scaling: {
                autoPause: cdk.Duration.minutes(10),
                minCapacity: rds.AuroraCapacityUnit.ACU_2,
                maxCapacity: rds.AuroraCapacityUnit.ACU_8,
            },
            credentials: rds.Credentials.fromSecret(dbSecret),
            defaultDatabaseName: 'Lavapool',
            securityGroups: [dbSecurityGroup],
        });


        const dockerLambda = new lambda.DockerImageFunction(this, 'Lavapool-Django', {
            code: lambda.DockerImageCode.fromImageAsset('.'),
            timeout: cdk.Duration.seconds(30),
            vpc,
            environment: {
                'SETTINGS': 'prod',
                'POSTGRES_HOST': auroraCluster.clusterEndpoint.hostname,
                'POSTGRES_PORT': auroraCluster.clusterEndpoint.port.toString(),
                'POSTGRES_USER': 'lavapool',
                'POSTGRES_DB': 'Lavapool',
                'POSTGRES_PASSWORD': dbSecret.secretValueFromJson('password').unsafeUnwrap(),
                // tODO query secret manager from django with boto instead of unsafeUnwrap().
            },
        });

        const httpApi = new apigateway.HttpApi(this, 'MyHttpApi', {
            apiName: 'Lavapool-Django-API',
            createDefaultStage: true,  // Automatically creates an HTTP API stage
        });

        httpApi.addRoutes({
            path: '/{proxy+}',
            methods: [apigateway.HttpMethod.ANY],
            integration: new integrations.HttpLambdaIntegration('Lavapool-Admin', dockerLambda),
        });

        new cdk.CfnOutput(this, 'Lavapool-ApiUrl', {
            value: httpApi.url!,
            description: 'The HTTP API Gateway URL',
        });
    }
}
