# Import the Boto3 library to interact with AWS services
import boto3
import json

def lambda_handler(event, context):
    # TODO implement
    # Create an S3 client using Boto3
    s3 = boto3.client('s3')

    # Retrieve a list of all S3 buckets in the account
    response = s3.list_buckets()

    # Extract the list of bucket dictionaries from the response
    buckets = response["Buckets"]

    bucket_names = []
    # Loop through each bucket and print its name
    for bucket in buckets:
        print(bucket["Name"])
        bucket_names.append(bucket["Name"])
    
    return {
        'statusCode': 200,
        'body': json.dumps(bucket_names, indent=4)
    }