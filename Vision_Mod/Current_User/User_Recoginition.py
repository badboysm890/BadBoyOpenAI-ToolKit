import face_recognition
import cv2
import numpy as np
import os
import redis
import struct
import os
os.chdir("/home/badboy17g/HackoHolics/Vision_Mod/Current_User")

r = redis.Redis(host='localhost', port=6379, db=0)


def fromRedis(r,n):
   encoded = r.get(n)
   h, w = struct.unpack('>II',encoded[:8])
   a = np.frombuffer(encoded, dtype=np.uint8, offset=8).reshape(h,w,3)
   return a

def toRedis(r,a,n):
   """Store given Numpy array 'a' in Redis under key 'n'"""
   h, w = a.shape[:2]
   shape = struct.pack('>II',h,w)
   encoded = shape + a.tobytes()

   # Store encoded data in Redis
   r.set(n,encoded)



while True:
    
    
    user = []
    img = fromRedis(r,'image')
    cv2.imwrite('Unknown/curent.jpg', img)
    Known = os.listdir("Known_Members")
    Unknown = os.listdir("Unknown")
    ypath = "Unknown/curent.jpg"
    
    for x in Known:
        xpath = "Known_Members/"+x
        known_image = face_recognition.load_image_file(xpath)
        known_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_image = face_recognition.load_image_file(ypath)
        try:
         unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
         results = face_recognition.compare_faces([known_encoding], unknown_encoding)
        
        except:
          print("Image serialization Failed")  
          results = ["none"]
        
        if results[0] == True:
            name = x.strip(".jpeg")
            user.append(name)
    if user == []:
        user.append("Unknown")


    r.set("Current_People",user[0])
    print(user[0])
    try:
     r.set("Current_People1",user[1])
     print(user[1])
     
    except:
      print("Exception Pipeline")       
        


    

