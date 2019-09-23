# V.2
import socketio
import redis
import subprocess
import time
from threading import Thread
import os
 
sio = socketio.Client()
redis = redis.Redis(host='localhost', port=6379, db=0)

def module(file):
#     command = "terminator --title='module' --working-directory='/home/badboy17g/Documents/Clara-V0.3/SpineV0.3' -e 'python3 " + file  
    print(file)
    subprocess.run(file, shell=True)
    sio.emit('PrepareRequest', {"message": "Module, Loaded Sir"})
    


def Loader(data):
 
 file = data
 
 Module = Thread(target = module(file))  
 Module.start()
 Module.join()
 
@sio.event
def connect():
     print("Connected to core(Module Loader))")
     
 

sio.connect('http://localhost:5000')  

@sio.on('ModuleLoad')
def on_IntHandler(data):
    print("got input")
    print(data)
    a=data["message"]
    print(a)
    module(a)
     