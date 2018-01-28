#!/usr/bin/python3

"""
Purpose - Click a picture using Raspi Cam module for every message in the queue
"""

import boto3
import picamera

#Get service resource
sqs = boto3.resource('sqs')

#Get our queue
queue = sqs.get_queue_by_name(QueueName='q-surveillance-on-demand')

#Get your camera
camera = picamera.PiCamera()

#Process message by simply clicking a picture using raspi cam module
for message in queue.receive_messages():
    print(message)
    #Click a picture in response to queue message
    camera.capture('captured_images/living-room.jpg')

    #Let the queue know that message is processed
    message.delete()
