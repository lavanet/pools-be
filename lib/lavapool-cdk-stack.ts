import {Construct} from 'constructs';
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apigateway from 'aws-cdk-lib/aws-apigatewayv2';
import * as integrations from 'aws-cdk-lib/aws-apigatewayv2-integrations';
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as secretsmanager from "aws-cdk-lib/aws-secretsmanager";
import * as rds from "aws-cdk-lib/aws-rds";
import * as s3 from 'aws-cdk-lib/aws-s3';

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

        const djangoSecret = new secretsmanager.Secret(this, 'Lavapool-DjangoSecrets', {
            generateSecretString: {
                secretStringTemplate: JSON.stringify({
                    username: 'lavapool'
                }),
                excludePunctuation: true,
                includeSpace: false,
                generateStringKey: 'secretkey',
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

        const bucket = new s3.Bucket(this, 'Lavapool-PublicBucket', {
            bucketName: 'lavapool-0b86ez',
            publicReadAccess: true,
            blockPublicAccess: {
                blockPublicAcls: false,
                blockPublicPolicy: false,
                ignorePublicAcls: false,
                restrictPublicBuckets: false,
            }
        });


        const apiLambda = new lambda.DockerImageFunction(this, 'Lavapool-Django', {
            code: lambda.DockerImageCode.fromImageAsset('.'),
            timeout: cdk.Duration.seconds(60),
            memorySize: 256,
            vpc,
            environment: {
                'SETTINGS': 'prod',
                'DJANGO_SECRETS': djangoSecret.secretArn,
                'DB_SECRETS': dbSecret.secretArn,
                'DB_HOST': auroraCluster.clusterEndpoint.hostname,
                'AWS_STORAGE_BUCKET_NAME': bucket.bucketName,
            },
        });

        dbSecret.grantRead(apiLambda);
        djangoSecret.grantRead(apiLambda);
        bucket.grantReadWrite(apiLambda);

        const httpApi = new apigateway.HttpApi(this, 'MyHttpApi', {
            apiName: 'Lavapool-Django-API',
            createDefaultStage: true,  // Automatically creates an HTTP API stage
        });

        httpApi.addRoutes({
            path: '/{proxy+}',
            methods: [apigateway.HttpMethod.ANY],
            integration: new integrations.HttpLambdaIntegration('Lavapool-Admin', apiLambda),
        });

        new cdk.CfnOutput(this, 'Lavapool-ApiUrl', {
            value: httpApi.url!,
            description: 'The HTTP API Gateway URL',
        });


    }
}
