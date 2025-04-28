from helpers import * 

def create_instances(ec2_client, ami_type="ubuntu", instance_amount=1):
    for i in range(instance_amount):
        if ami_type.lower().strip() == "ubuntu":
            create_ubuntu_instance(ec2_client)
            print("Create Ubuntu")
        elif ami_type.lower().strip() == "linux 2023":
            create_amazon_linux_2023_instance(ec2_client)
            print("Create Linux 2023")
        elif ami_type.lower().strip() == "linux 2":
            create_amazon_linux_2_instance(ec2_client)
            print("Create Linux 2")
        else:
            print("Invalid AMI Type")
            break

if "__main__" == __name__:
    ec2_client = get_ec2_client()
    create_instances(ec2_client)
    create_instances(ec2_client, ami_type="Ubuntu")
    create_instances(ec2_client, ami_type="ubuNtu")
    create_instances(ec2_client, ami_type="ubuNtu ")
    create_instances(ec2_client, ami_type="Linux 2")
    create_instances(ec2_client, ami_type="Windows 11")
    create_instances(ec2_client, ami_type="Linux 2023", instance_amount=2)
    create_instances(ec2_client, ami_type="Linux 2025", instance_amount=3)