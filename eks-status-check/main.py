import boto3

client = boto3.client('eks')

# Print the available clusters
clusters = client.list_clusters()
print(clusters['clusters'])

# for every single cluster
for cluster in clusters:

    # describe a single cluster
    response = client.describe_cluster(
        name=cluster
    )

    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['endpoint']
    cluster_version = cluster_info['version']

    print(f"Cluster {cluster} status is {cluster_status}")
    print(f"Cluster version: {cluster_version}")