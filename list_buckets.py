# Import the Boto3 library to interact with AWS services
import boto3

# Create an S3 client using Boto3
s3 = boto3.client('s3')

# Retrieve a list of all S3 buckets in the account
response = s3.list_buckets()

# Extract the list of bucket dictionaries from the response
buckets = response["Buckets"]

# Loop through each bucket and print its name
for bucket in buckets:
    print(bucket["Name"])
