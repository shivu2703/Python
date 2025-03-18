import boto3
import json 

ec2_client = boto3.client('ec2')

def list_instances():
    response = ec2_client.describe_instances()
    # print(json.dumps(response, default=str, indent=4))
    # print(len(response['Reservations'][0]['Instances']))
    # print(json.dumps(response['Reservations'][0], default=str, indent=4))
    # print(json.dumps(response['Reservations'][1], default=str, indent=4))
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print("Instance ID: "+ instance['InstanceId'])
            print("Instance state: "+ instance['State']['Name'])

list_instances()