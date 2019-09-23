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
import os
os.chdir("/home/badboy17g/HackoHolics/Module_Loader/modules/Hotword")
def VoiceSynth():    
  print("HotWord Called")


interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

model = "Praveen.pmdl"
callbacks = [lambda: VoiceSynth()]
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print(' Listening')

detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
