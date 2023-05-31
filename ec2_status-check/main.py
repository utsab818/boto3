# Check status of ec2 instances in default region
import boto3
import schedule


# Client and resource initialization
ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

# Instance status check using describe_instance_status
def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances = True
    )
    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status is {sys_status}")
        
    print("------------###------------")

# Runs the status check every 5 minutes
schedule.every(5).minutes.do(check_instance_status) 

while True:
    schedule.run_pending()