import boto3
import json

ec2_client = boto3.client('ec2')

instance_id = 'i-036e969daaaa4f38b'

response = ec2_client.describe_instances( InstanceIds=[instance_id])

# print(json.dumps(response['Reservations'][0]['Instances'][0],default=str, indent=4))
# print(json.dumps(response, default=str, indent=4))
print(f"Public IP of instance is: {response['Reservations'][0]['Instances'][0].get('PublicIpAddress')}")

