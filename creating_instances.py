from helpers import *  # Import all helper functions (assumes create instance functions are defined here)

def create_instances(ec2_client: object, ami_type: str = "ubuntu", instance_amount: int = 1) -> None:
    """
    Create EC2 instances based on the specified AMI type.

    Args:
        ec2_client (object): An initialized EC2 client used to launch instances.
        ami_type (str, optional): Type of AMI to use ("ubuntu", "linux 2023", "linux 2"). Defaults to "ubuntu".
        instance_amount (int, optional): Number of instances to create. Defaults to 1.

    Returns:
        None
    """
    for i in range(instance_amount):
        ami = ami_type.lower().strip()  # Normalize input for case-insensitive matching
        if ami == "ubuntu":
            create_ubuntu_instance(ec2_client)  # Create Ubuntu instance
            print("Create Ubuntu")
        elif ami == "linux 2023":
            create_amazon_linux_2023_instance(ec2_client)  # Create Amazon Linux 2023 instance
            print("Create Linux 2023")
        elif ami == "linux 2":
            create_amazon_linux_2_instance(ec2_client)  # Create Amazon Linux 2 instance
            print("Create Linux 2")
        else:
            print("Invalid AMI Type")  # Invalid AMI type provided, exit the loop
            break

if __name__ == "__main__":
    ec2_client = get_ec2_client()  # Get a boto3 EC2 client

    # Test cases to create different types of instances
    create_instances(ec2_client)
    create_instances(ec2_client, ami_type="Ubuntu")
    create_instances(ec2_client, ami_type="ubuNtu")
    create_instances(ec2_client, ami_type="ubuNtu ")
    create_instances(ec2_client, ami_type="Linux 2")
    create_instances(ec2_client, ami_type="Windows 11")
    create_instances(ec2_client, ami_type="Linux 2023", instance_amount=2)
    create_instances(ec2_client, ami_type="Linux 2025", instance_amount=3)
