#!/usr/bin/python3

"""
Purpose - Click a picture using Raspi Cam module for every message in the queue
"""

import boto3
import picamera
import time
import datetime

#Get service resource
sqs = boto3.resource('sqs')

#Get our queue
queue = sqs.get_queue_by_name(QueueName='q-surveillance-on-demand')

#Get your camera
camera = picamera.PiCamera()

#Keep polling queue for new messages
while True:
    #Capture timestamp
    ts = time.time()
    image_suffix = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
    image_name = "living-room_" + image_suffix + ".jpg"
    #Process message by simply clicking a picture using raspi cam module
    for message in queue.receive_messages():
        print(message)
        #Click a picture in response to queue message
        camera.capture('captured_images/' + image_name)

        #Let the queue know that message is processed
        message.delete()
        
        #wait for 10 seconds
        time.sleep(10)
