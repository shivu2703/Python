# 1 - Modify the volume size
# 2 - Wait for the volume to be in optimized or in use state
# 3 - Expand the partition
# 4 - Resize the file system

# 1 - Modify the volume size- get instance id , from instance id get volume id and then modify voulme with volume id

import boto3
import subprocess
import time

def run_cmd(cmd):
   result = subprocess.run(cmd, shell=True, capture_output=True , text=True, check=True)
   return result.stdout.strip()

def get_instance_id():
    # Step 1: Get the token
    token_cmd = (
        "curl -X PUT 'http://169.254.169.254/latest/api/token' "
        "-H 'X-aws-ec2-metadata-token-ttl-seconds: 21600'"
    )
    token = run_cmd(token_cmd)

    # Step 2: Use the token to get the instance ID
    metadata_cmd = (
        "curl -H 'X-aws-ec2-metadata-token: {}' "
        "http://169.254.169.254/latest/meta-data/instance-id".format(token)
    )
    return run_cmd(metadata_cmd)







# Main function

if __name__ == "__main__":
   print(get_instance_id())
