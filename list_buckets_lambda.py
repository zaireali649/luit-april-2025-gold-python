# Import the Boto3 library to interact with AWS services
import boto3
import json
from typing import Any, Dict

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda handler to list all S3 bucket names in the account.

    Args:
        event (dict): AWS Lambda event object (not used in this function).
        context (object): AWS Lambda context object (not used in this function).

    Returns:
        dict: A JSON-serializable dictionary containing the HTTP status code and a list of bucket names.
    """

    # Create an S3 client using Boto3
    s3 = boto3.client('s3')

    # Retrieve a list of all S3 buckets in the account
    response = s3.list_buckets()

    # Extract the list of bucket dictionaries from the response
    buckets = response["Buckets"]

    # Initialize a list to store bucket names
    bucket_names = []

    # Loop through each bucket dictionary and extract the name
    for bucket in buckets:
        print(bucket["Name"])  # Log the bucket name
        bucket_names.append(bucket["Name"])  # Add the name to the list
    
    # Return the list of bucket names in the response body
    return {
        'statusCode': 200,
        'body': json.dumps(bucket_names, indent=4)
    }
