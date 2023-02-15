# Name: Edward E. Daisey
# Date: February 15th, 2023
# Description: Practice with Boto3 & Python. In Progress.

import boto3

# Purpose - Create a connection to the EC2 service.
ec2 = boto3.resource('ec2')

# Purpose - Launch a new EC2 instance.
instance = ec2.create_instances(
    ImageId='ami-0c94855ba95c71c99',       # This is the Amazon Machine Image (AMI) ID for Amazon Linux 2.
    MinCount=1,                            # This is the minimum number of instances to launch.
    MaxCount=1,                            # This is the maximum number of instances to launch.
    InstanceType='t2.micro',               # This is the instance type.
    KeyName='my-key-pair',                 # This is the name of the key pair to use for SSH access.
    SecurityGroups=['my-security-group']   # This is the name of the security group to apply to the instance.
)

# Purpose - Print the ID of the new instance.
print('Instance ID: ' + instance[0].instance_id)

# Working Notes --
# This is a Python script that uses the Boto3 library to interact with the Amazon Web Services (AWS) EC2 service to launch a new EC2 instance. 
# Here's what each part of the script does:
# import boto3: This line imports the Boto3 library, which provides a Python interface to AWS services.
# ec2 = boto3.resource('ec2'): This line creates a connection to the EC2 service, which is necessary to perform any operations on EC2 instances.
# instance = ec2.create_instances(...): This line launches a new EC2 instance with the specified parameters. 
# The parameters include the ID of the Amazon Machine Image (AMI) to use, the instance type, the name of the key pair to use for SSH access, and the 
# name of the security group to apply to the instance.
# print('Instance ID: ' + instance[0].instance_id): This line prints the ID of the newly created instance.
