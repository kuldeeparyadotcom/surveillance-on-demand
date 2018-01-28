# Assumptions - 
1. AWS Account is created.
2. IAM User is created and Access Key ID and Secret Access Key are set up on the machine (Raspberry Pi in this case) running this code.
For example - ~/.aws/config captures ACCESS_KEY_ID and SECRET_ACCESS_KEY.
3. Python3 is installed.
4. The following Python modules are instaled - boto3, python-picamera
5. aws-cli is installed and configured properly. i.e. pip3 install awscli --upgrade --user
https://docs.aws.amazon.com/cli/latest/userguide/installing.html
6. Amazon SQS Standar Queue is created that will be processed by this project. 


## Got curious? Some learning reources for you - 
1. https://docs.aws.amazon.com/cli/latest/reference/sqs/list-queues.html
2. http://boto3.readthedocs.io/en/latest/guide/sqs.html
3. https://www.raspberrypi.org/documentation/usage/camera/python/README.md
