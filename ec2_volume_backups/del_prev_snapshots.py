# delete previous snapshots and store only recent ones
import boto3
from operator import itemgetter

client = boto3.client('ec2')

# Fetch the volumes
volumes = client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['prod']
        }
    ]
)

for volume in volumes['Volumes']:
    snapshots = client.describe_snapshots(
        OwnerIds = ['self'] # only snapshots that we created // Not the ones aws made in default.
        Filters=[
        {
            'Name': 'volume-id',
            'Values': [volume['VolumeId']]
        }
    ]
    )

    # snapshots sorted by date
    # reverse = True will sort in descending order so that it will be easier to get the recent snapshots
    sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True) # itemgetter gets the key from dictionary(snapshots)

    # Print the dates without sorting
    for snap in shapshots['Snapshots']:
        print(snap['StartTime'])

    print("#######")

    # Print sorted snapshots
    for snap in sorted_by_date:
        print(snap['StartTime'])

    # Loop through the sorted snapshots 
    # Keep 2 snapshots (Skip in loop)
    # Delete all other snapshots
    print("Deleted snapshots:")
    for snap in sorted_by_date[2:]: # start from 2
        # delete the snapshots
        response = client.delete_snapshot(
            SnapshotId = snap['SnapshotId']
        )
        print(response)

