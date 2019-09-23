import redis
import time
import boto3
import json
import cv2
import struct
import numpy as np
import os

os.chdir("/home/badboy17g/HackoHolics/Vision_Mod/Neural_Mindset")

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
client=boto3.client('rekognition',
 aws_access_key_id="AKIAIGAQSNNU4ST43CMQ",
 aws_secret_access_key="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",
 region_name="ap-south-1")
Mood = ["Calm","Happy","Disgusted","Confused","Sad","Surprised","Fear","Angry"]

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


while True:
  

 
  img = fromRedis(r,'image')
  cv2.imwrite('curent.jpg', img)

  imageFile='curent.jpg'
    
  try:    
    with open(imageFile, 'rb') as image:
      response = client.detect_faces(Image={'Bytes': image.read()},Attributes=['ALL'])

    for faceDetail in response['FaceDetails']:
                    
      Emotion = {
      "Emotions" :  faceDetail['Emotions'],
      "Eye"      :  faceDetail['EyesOpen'],
      "Mouth"    :  faceDetail['MouthOpen'],
      "Smile"    :  faceDetail['Smile'] 
      }
      a = Emotion["Emotions"]
      j=json.dumps(a)
      jl = json.loads(j)
      for i in jl:
        types = i["Type"]
        confidence = i["Confidence"]
        types = "user"+types 
        r.set(types,round(confidence))

  except:
    print("error in visonAI")                
  
  
  MoodScore = []
  userCALM = r.get("userCALM")
  userCALM = userCALM.decode("utf-8")
  MoodScore.append(int(userCALM))
  userHAPPY = r.get("userHAPPY")
  userHAPPY = userHAPPY.decode("utf-8")
  MoodScore.append(int(userHAPPY))
  userDISGUSTED = r.get("userDISGUSTED")
  userDISGUSTED = userDISGUSTED.decode("utf-8")
  MoodScore.append(int(userDISGUSTED))
  userCONFUSED = r.get("userCONFUSED")
  userCONFUSED = userCONFUSED.decode("utf-8")
  MoodScore.append(int(userCONFUSED))
  userSAD = r.get("userSAD")
  userSAD = userSAD.decode("utf-8")
  MoodScore.append(int(userSAD))
  userSURPRISED = r.get("userSURPRISED")
  userSURPRISED = userSURPRISED.decode("utf-8")
  MoodScore.append(int(userSURPRISED))
  userFEAR = r.get("userFEAR")
  userFEAR = userFEAR.decode("utf-8")
  MoodScore.append(int(userFEAR))
  userANGRY = r.get("userANGRY")
  userANGRY = userANGRY.decode("utf-8")
  MoodScore.append(int(userANGRY))
  
  Max = max(MoodScore)
  dex = MoodScore.index(Max)
  print("User is "+Mood[dex])
  time.sleep(120)
  