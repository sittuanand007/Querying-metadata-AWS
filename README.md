# Querying-metadata-AWS
Code to query metadata of certain instance or resource in AWS.

This code will first import the boto3 module. The boto3 module is used to interact with AWS services, such as EC2.
              
              The "get_instance_metadata()" function uses the "ec2_client" object to get the metadata for the current instance. 
              The "describe_instances()" method returns a list of instances, and the Tags property of each instance contains a list of tags. 
              The Name tag is used to get the name of the instance.

              The main() function then prints the metadata for the current instance in formatted output.


  Execution of this code will print the JSON response from the metadata service in formatted output.
