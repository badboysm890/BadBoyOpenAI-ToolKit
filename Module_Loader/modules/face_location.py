import face_recognition
import cv2
import PIL 
import struct
import redis
import numpy as np
import os 
from nanpy import SerialManager
connection = SerialManager(device='/dev/ttyACM0')
from nanpy import Servo
import time
servo = Servo(7)
url = 'http://10.42.0.202:8080/video'
r = redis.Redis(host='localhost', port=6379, db=0)
os.chdir("/home/badboy17g/HackoHolics/Module_Loader/modules")
prev = 0
def fromRedis(r,n):
   encoded = r.get(n)
   h, w = struct.unpack('>II',encoded[:8])
   a = np.frombuffer(encoded, dtype=np.uint8, offset=8).reshape(h,w,3)
   return a

while True:
 a = 0 
 b = 0   
 img = fromRedis(r,'image')
 img = cv2.resize(img, (360,200))
 cv2.imwrite('image.jpg', img)
 image = face_recognition.load_image_file("image.jpg")
 face_locations = face_recognition.face_locations(image)
 print(face_locations)
 try:
  loc = face_locations[0]
  print(loc[1])
  if prev > loc[1]:
   a = loc[1]
   b = prev
  else:
   a = prev
   b = loc[1]
  for i in range(a,b):
    servo.write(160 - loc[1]/2)
    print(160 - loc[1]/2)
  prev = 180 - loc[1]
 except:
  print("No body there")   
 