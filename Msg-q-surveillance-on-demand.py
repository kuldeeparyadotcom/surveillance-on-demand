#!/usr/bin/python3

"""
Purpose - Send a meesage to a queue 
"""

import boto3

#Get service resource
sqs = boto3.resource('sqs')

#Get our queue
queue = sqs.get_queue_by_name(QueueName='q-surveillance-on-demand')

#Create our msg
response = queue.send_message(MessageBody='testing')

#Prinout message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))
