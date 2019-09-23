from nanpy import ArduinoApi
from nanpy import SerialManager
# from nanpy import Ultrasonic
import boto3
import playsound
from time import sleep
from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)
connection = SerialManager(device='/dev/ttyACM0')
class Ultrasonic(ArduinoObject):
    cfg_h_name = 'USE_Ultrasonic'

    def __init__(self, echo, trig, useInches, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', echo, trig, useInches)

    @returns(float)
    @arduinoobjectmethod
    def get_distance(self):
        pass

    def reading_in_range(self, low, high):
        return low <= self.get_distance() <= high
        

trigPin = 9
echoPin = 10
polly_client = boto3.Session(
                aws_access_key_id="AKIAIGAQSNNU4ST43CMQ",
aws_secret_access_key="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",
    region_name="ap-south-1").client('polly')



a = ArduinoApi(connection=connection)
ultrasonic = Ultrasonic(echoPin, trigPin, False, connection=connection)
while True:
 distance = ultrasonic.get_distance()
 print(distance)
 d = str(distance)
 sleep(0.002)
 if distance <= 100:
    response = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3', 
                Text = "There is obstacle near "+d+" Centimeters")
    file = open('play.mp3', 'wb')
    file.write(response['AudioStream'].read())
    file.close()              
    print("prepare complete")
    playsound.playsound("play.mp3")
     