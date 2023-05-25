import boto3

ec2_client = boto3.client('ec2') #default region
resource_client = boto3.resource("ec2")

new_vpc = resource_client.create_vpc(
    CidrBlock="10.0.0.0/16"
)

sub1 = new_vpc.create_subnet(
    CidrBlock="10.0.1.0/24"
)

sub2 = new_vpc.create_subnet(
    CidrBlock="10.0.2.0/24"
)

new_vpc.create_tags(
    Tags=[
        {
            'Key': 'Name',
            'Value': 'my-vpc'
        }
    ]
)

sub1.create_tags(
    Tags=[
        {
            'Key': 'Name',
            'Value': 'my-vpc'
        }
    ]
)

sub2.create_tags(
    Tags=[
        {
            'Key': 'Name',
            'Value': 'my-vpc'
        }
    ]
)



all_vpcs = ec2_client.describe_vpcs()

vpcs = all_vpcs["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_assoc_sets = (vpc["CidrBlockAssociationSet"])
    for assoc_set in cidr_block_assoc_sets:
        print(assoc_set["CidrBlockState"])

