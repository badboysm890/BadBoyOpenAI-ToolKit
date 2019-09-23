# V.2
import socketio
import pymongo
import redis
import time
import boto3

from playsound import playsound

sio = socketio.Client()
r = redis.Redis(host='localhost', port=6379, db=0)
polly_client = boto3.Session(
                aws_access_key_id="AKIAIGAQSNNU4ST43CMQ",
aws_secret_access_key="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",
    region_name="ap-south-1").client('polly')

def prepare(data):
    
 response = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3', 
                Text = data)
 file = open('play.mp3', 'wb')
 file.write(response['AudioStream'].read())
 file.close()               
 r.set("Speak","True")
 print("prepare complete")
 playsound("play.mp3")
 r.set("Ts_state","True")
 
@sio.event
def connect():
     print("Connected to (Voice Prepare) Core")
     

sio.connect('http://localhost:5000')  

@sio.on('PrepareRequest')
def on_PrepareReq(data):

 print(data["message"])
 prepare(data["message"])
