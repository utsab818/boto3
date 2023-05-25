import boto3

# ec2_client = boto3.client('ec2'), region_name="")
ec2_client = boto3.client('ec2') #default region

all_vpcs = ec2_client.describe_vpcs()

vpcs = all_vpcs["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_assoc_sets = (vpc["CidrBlockAssociationSet"])
    for assoc_set in cidr_block_assoc_sets:
        print(assoc_set["CidrBlockState"])

