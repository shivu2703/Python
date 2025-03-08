import boto3

ec2_client = boto3.client('ec2')

def manage_instance(instance_id, action):
    if action == "start":
        ec2_client.start_instances(InstanceIds=[instance_id])
        print(f"Starting Instance: {instance_id}")
    elif action == "stop":
        ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping Instance: {instance_id}")
    elif action == "terminate":
        ec2_client.terminate_instances(InstanceIds=[instance_id])
        print(f"Terminating Instance: {instance_id}")
    else:
        print("Invalid actions, Use 'start' or 'stop' or 'terminate'.")

manage_instance('i-02430e493171ae54a', "terminate")