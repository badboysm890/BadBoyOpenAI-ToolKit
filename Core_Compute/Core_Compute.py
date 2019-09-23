from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context,request
from random import random
from time import sleep
import json
import sys
import eventlet
from threading import Thread, Event     
import os

__author__ = 'BadBoy'


app = Flask(__name__)


app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

socketio = SocketIO(app)

thread = Thread()
thread_stop_event = Event()
message = "hello" 
messages = []       
  

@socketio.on('Ears')
def handle_message(message):
   
    print('I Heard :'+ message["message"])
    emit('NLU_Request', {"message": message["message"]}, broadcast=True)

@socketio.on('Voice')
def handle_Voice(message):
   
    print('PrepareVoice :'+ message["message"])
    emit('PrepareRequest', {"message": message["message"]}, broadcast=True)    

@socketio.on('IntHandlerRequest')
def handle_Intent(message):
   
    print('Handling Intent :'+ message["message"])
    emit('IntHandlerRequest', {"message": message["message"]}, broadcast=True)    

@socketio.on('ModuleLoad')
def handle_Module(message):
   
    print('ModuleLoad :'+ message["message"])
    emit('ModuleLoad', {"message": message["message"]}, broadcast=True)    
    

@socketio.on('connect')
def test_connect():
    
    print('Client connected')
        
    if not thread.isAlive():
        print("Starting Thread")


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
   socketio.run(app, host='localhost',debug=True,port=5000)
