import boto3

ec2_client= boto3.client('ec2')

instance = ec2_client.run_instances(
    ImageId ='ami-0e2c8caa4b6378d8c',
    InstanceType ='t2.micro',
    MinCount = 1,
    MaxCount = 1
)
for inst in instance.get("Instances"):
    print(F"Instance {inst.get('InstanceId')} is launching")