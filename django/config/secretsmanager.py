import base64
import json

import boto3
from botocore.exceptions import ClientError


def get_secret(secret_name):
    """
    Retrieve a secret from AWS Secrets Manager.
    """
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager')
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        if e.response['Error']['Code'] in ['DecryptionFailureException', 'InternalServiceErrorException',
                                           'InvalidParameterException', 'InvalidRequestException',
                                           'ResourceNotFoundException', ]:
            raise e
    else:
        # Secrets Manager returns the secret as a string
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return json.loads(secret)
        else:
            # Handle binary secrets if necessary
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            return json.loads(decoded_binary_secret)

