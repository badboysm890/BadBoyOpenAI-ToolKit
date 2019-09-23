import redis
import socketio
import boto3
import playsound

redis = redis.Redis(host='localhost', port=6379, db=0) 
user = redis.get("Current_People")
user = user.decode('UTF-8')
user = user + " is near you"
print(user)
polly_client = boto3.Session(
                aws_access_key_id="AKIAIGAQSNNU4ST43CMQ",
aws_secret_access_key="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",
    region_name="ap-south-1").client('polly')
response = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3', 
                Text = user)
file = open('play.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()               
redis.set("Speak","True")
print("prepare complete")
playsound.playsound("play.mp3")
redis.set("Ts_state","True")    