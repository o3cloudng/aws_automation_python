import json

import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    print(event)

    user = event['detail']['userIdentity']['userName']

    instanceId = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']

    ec2.create_tags(
        Resources=[
        'string',
        ],
        Tags=[
            {
                'Key': 'owner',
                'Value': user
            },
        ]
    )
