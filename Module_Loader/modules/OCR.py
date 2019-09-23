import textract
import cv2 
import numpy as np
import struct
import redis
import boto3
import playsound
import os
os.chdir("/home/badboy17g/HackoHolics/Module_Loader/modules")

r = redis.Redis(host='localhost', port=6379, db=0)
def fromRedis(r,n):
   encoded = r.get(n)
   h, w = struct.unpack('>II',encoded[:8])
   a = np.frombuffer(encoded, dtype=np.uint8, offset=8).reshape(h,w,3)
   return a

while True:
 img = fromRedis(r,'image')
 img = cv2.resize(img, (640,480))
 cv2.imwrite("image.png",img)
 text = textract.process("image.png")
 text = text.decode('utf8')
 text = text.strip("\r\n")
 print(text)
 

