import cv2
from time import sleep
import struct
import redis
import numpy as np
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
cam = cv2.VideoCapture(0)

def toRedis(r,a,n):
   """Store given Numpy array 'a' in Redis under key 'n'"""
   h, w = a.shape[:2]
   shape = struct.pack('>II',h,w)
   encoded = shape + a.tobytes()

   # Store encoded data in Redis
   r.set(n,encoded)



def fromRedis(r,n):
   encoded = r.get(n)
   h, w = struct.unpack('>II',encoded[:8])
   a = np.frombuffer(encoded, dtype=np.uint8, offset=8).reshape(h,w,3)
   return a

    # Redis connection
while True:
 
 ret, img = cam.read()
 toRedis(r, img, 'image')



