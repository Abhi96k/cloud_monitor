import boto3
from botocore.exceptions import ClientError

# Initialize the ECR client for the 'ap-south-1' region
ecr_client = boto3.client('ecr', region_name='ap-south-1')

def create_ecr_repository(repository_name):
    try:
        response = ecr_client.create_repository(
            repositoryName=repository_name
        )
        print(f"Repository '{repository_name}' created successfully!")
        return response['repository']
    except ClientError as e:
        print(f"An error occurred: {e}")
        return None

# Replace with your desired repository name
repository_name = 'flask-monitoring-repo'

# Create the repository
repository = create_ecr_repository(repository_name)
if repository:
    print("Repository URI:", repository['repositoryUri'])
