import boto3
import json

def get_instance_metadata():
    """Gets the metadata for the current instance using Boto3."""
    session = boto3.Session()
    ec2_client = session.client("ec2")
    response = ec2_client.describe_instances()

    metadata = {}
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            for tag in instance["Tags"]:
                if tag["Key"] == "Name":
                    metadata["Name"] = tag["Value"]

    return metadata

def main():
    """Prints the metadata for the current instance in JSON format using Boto3."""
    metadata = get_instance_metadata()

    if metadata is not None:
        print(json.dumps(metadata, indent=4))
    else:
        print("Failed to get instance metadata.")

if __name__ == "__main__":
    main()
