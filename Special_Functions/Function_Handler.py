import socketio
import pymongo
import redis

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
sio = socketio.Client()
mydb = myclient["Hack_O_Holics"]
redis = redis.Redis(host='localhost', port=6379, db=0)


def HandleIntent(intent):
 x=""   
 data = mydb["Special_Functions"]
 for x in data.find({ "Intent": intent }):
   print(x["File"]+intent)
   sio.emit('ModuleLoad', {"message": x["File"]})
   
 if x=="":  
  print("no file located")
  print("falling back")
  sio.emit('Voice', {"message": "No Special Found"})
   

@sio.event
def connect():
     print("Connected to Core(intent handler Loader))")
     

sio.connect('http://localhost:5000')  



@sio.on('IntHandlerRequest')
def on_IntHandler(data):
     a=data["message"]
     print(a)
     HandleIntent(a)