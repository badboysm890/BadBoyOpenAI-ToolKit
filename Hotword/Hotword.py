import playsound
import snowboydecoder
import sys
import signal
import speech_recognition as sr
import socketio
import redis
import time
import random

time.sleep(10)
r = sr.Recognizer()
sio = socketio.Client()
redis = redis.Redis(host='localhost', port=6379, db=0)


def VoiceSynth():    
 
   a = str(random.randrange(1,5))
   with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source) 
      print("Im Ready")
      playsound.playsound("1.mp3")
      time.sleep(1.3)
      audio = r.listen(source)

   try:
      Net=redis.get("Network") 
      Net = Net.decode("utf-8")
      print(Net)  
      if Net == "False": 
       print("Offline Mode Sorry")
       a=r.recognize_sphinx(audio)
       sio.emit('Ears', {"message": a})
      

      else: 
       print("Online Mode")  
       a=r.recognize_google(audio)
       print(a)
       sio.emit('Ears', {"message": a})
      
      
   except sr.UnknownValueError:
      a=""
      print("Sumi could not understand audio")
      
      
   except sr.RequestError as e:
      a=""
      print("Could not connect to service; {0}".format(e)) 

@sio.event
def connect():
    print("Connected to Spine (Hotword)")
   
sio.connect('http://localhost:5000')    


interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

model = "clara.pmdl"
callbacks = [lambda: VoiceSynth()]
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Sumi is Listening')

detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
