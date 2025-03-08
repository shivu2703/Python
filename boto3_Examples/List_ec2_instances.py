import boto3

ec2_client = boto3.client('ec2')

def list_instances():
    response = ec2_client.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print("Instance ID: "+ instance['InstanceId'])
            print("Instance state: "+ instance['State']['Name'])

list_instances()