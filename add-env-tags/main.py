# Add tags 
# Two region Mumbai and Tokyo
# Add tag as prod to mumbai ec2 instances
# Add tag as dev to tokyo ec2 instances

import boto3

# Mumbai region client and resource
ec2_client_mumbai = boto3.client('ec2', region_name='ap-south-1')
ec2_resource_mumbai = boto3.resource('ec2', region_name='ap-south-1')

# Tokyo region client and resource
ec2_client_tokyo = boto3.client('ec2', region_name='ap-northeast-1')
ec2_resource_tokyo = boto3.resource('ec2', region_name='ap-northeast-1')

# List to store instance ids
instance_ids_mumbai = []
instance_ids_tokyo = []

# Get to reservation
reservations_mumbai = ec2_client_mumbai.describe_instances()['Reservations']
reservations_tokyo = ec2_client_tokyo.describe_instances()['Reservations']

# iterate and append ids to above list
for res in reservations_mumbai:
    instances = res['Instances']
    for ins in instances:
        instance_ids_mumbai.append(ins['InstanceId'])


for res in reservations_tokyo:
    instances = res['Instances']
    for ins in instances:
        instance_ids_tokyo.append(ins['InstanceId'])

# create tags for mumbai
response = ec2_client_mumbai.create_tags(
    Resources= instance_ids_mumbai,
    Tags=[
    {
        'Key': 'environment',
        'Value': 'prod'
    },
]
)

# create tags for tokyo
response = ec2_client_tokyo.create_tags(
    Resources= instance_ids_tokyo,
    Tags=[
    {
        'Key': 'environment',
        'Value': 'dev'
    },
]
)