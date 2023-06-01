# Create the new volume from snapshots and attach to the ec2 volume
import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

instance_id = "i-02cdff0caaf9c469a" # Enter your instance id

volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)

instance_volume = volumes['Volumes'][0]

snapshots = client.describe_snapshots(
        OwnerIds = ['self'] # only snapshots that we created // Not the ones aws made in default.
        Filters=[
        {
            'Name': 'volume-id',
            'Values': [instance_volume['VolumeId']]
        }
    ]
)

latest_snapshot = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0] # itemgetter gets the key from dictionary(snapshots)
# [0] gives the latest snapshot
print(latest_snapshot['StartTime'])

new_volume = ec2_client.create_volume(
    SnapshotId = latest_snapshot['SnapshotId']
    AvailabilityZone = "ap-south-1"
    TagSpecifications = [
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'prod'
                }
            ]
        }
    ]
)

# wait for new_volume to be in available state and attach the volume to ec2
while True:
    vol = ec2_resource.Volume(new_volume['VolumeId'])
    print(vol.state)
    if(vol.state == 'available'):
        ec2_resource.Instance(instance_id).attach_volume(
        VolumeId = new_volume['VolumeId'],
        Device = '/dev/sda2'
        )
        break