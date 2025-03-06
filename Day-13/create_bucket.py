import boto3

client = boto3.client('s3')
bucket_name = "shivu-boto3-py-123"

response = client.create_bucket(
    Bucket = bucket_name
)

print(response)