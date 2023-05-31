import boto3
import schedule

client = boto3.client('ec2')

def create_volume_snapshots():

    # if snapshots only for prod server
    volumes = client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )

    # for every volume create snapshot
    for volume in volumes['Volumes']:
        new_snapshot = client.create_snapshot(
            VolumeId = volume['VolumeId']
        )

        print(new_snapshot)

# set the schedule
schedule.every().day.do(create_volume_snapshots)
# schedule.every(20).seconds.do(create_volume_snapshots)

while True:
    schedule.run_pending()