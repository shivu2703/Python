import boto3

client = boto3.client('s3')

response = client.delete_bucket(
    Bucket = "shivu-boto3-py-123"
)

print(response)