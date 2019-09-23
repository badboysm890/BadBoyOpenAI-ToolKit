import face_recognition
import cv2
import numpy as np
import os
import time 
import redis
import struct
from PIL import Image

r = redis.Redis(host='localhost', port=6379, db=0)
os.chdir("/home/badboy17g/HackoHolics/Module_Loader/modules")
def fromRedis(r,n):
   encoded = r.get(n)
   h, w = struct.unpack('>II',encoded[:8])
   a = np.frombuffer(encoded, dtype=np.uint8, offset=8).reshape(h,w,3)
   return a

user = []
img = fromRedis(r,'image')
cv2.imwrite('temp/curent.jpg', img)
Known = os.listdir("Known_Members")
ypath = "temp/curent.jpg"
    
for x in Known:
    xpath = "Known_Members/"+x
    known_image = face_recognition.load_image_file(xpath)
    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_image = face_recognition.load_image_file(ypath)
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([known_encoding], unknown_encoding)
    
    if results[0] == True:
        name = x.strip(".jpeg")
        user.append(name)
    if user == []:
        user.append("Unknown")
print(user)
if user[0] == "Unknown":

    s_term=r.get("Query")
    s_term = s_term.decode("utf-8")  
    text = []
    text = s_term.split(' ')
    print(text)
    index = len(text)-1
    name_people = text[index] 
    img = fromRedis(r,'image')
    name_people = name_people+".jpg"
    cv2.imwrite("temp/"+name_people, img)
    image = face_recognition.load_image_file("temp/"+name_people)
    face_locations = face_recognition.face_locations(image)
    for face_location in face_locations:

        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save("Known_Members/"+name_people)
else :
    print("i know you already")
    r.set("Query", "i know you already")

time.sleep(5)