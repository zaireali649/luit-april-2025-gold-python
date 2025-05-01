from typing import List, Dict, Any
from helpers import *


def print_bucket_names(s3_client: Any) -> None:
    """
    Prints the names of all S3 buckets returned by the list_buckets helper function.

    Args:
        s3_client (Any): Boto3 S3 client object or equivalent.
    """
    bucket_names: List[str] = list_buckets(s3_client) # same as "\n".join(bucket_names)

    for bucket_name in bucket_names:
        print(bucket_name)


def print_instance_ids(ec2_client: Any) -> None:
    """
    Prints the instance IDs from a list of EC2 instances returned by the describe_instances helper function.

    Args:
        ec2_client (Any): Boto3 EC2 client object or equivalent.
    """
    instances: List[Dict[str, Any]] = describe_instances(ec2_client)

    instance_ids: List[str] = []
    for instance in instances:
        instance_ids.append(instance['InstanceId'])

    for instance_id in instance_ids:
        print(instance_id)


if __name__ == "__main__":
    ec2_client: Any = get_ec2_client()
    s3_client: Any = get_s3_client()

    print_bucket_names(s3_client)
    print_instance_ids(ec2_client)
