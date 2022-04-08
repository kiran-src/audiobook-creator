import os
import boto3

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

# poly = boto3.client('polly')
print(boto3.client('polly'))