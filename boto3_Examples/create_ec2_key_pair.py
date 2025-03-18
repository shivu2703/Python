import boto3
import json
 
ec2_client = boto3.client('ec2')

response = ec2_client.create_key_pair(
    KeyName='shivu-demo-2',
    TagSpecifications=[
        {
            'ResourceType': 'key-pair',
            'Tags': [
                {
                    'Key': 'Env',
                    'Value': 'Dev'
                },
            ]
        },
    ])

# print(json.dumps(response, default=str, indent=4))

print(f"Key pair Name: { response['KeyName']} and Key Material is: { response['KeyMaterial']} ")