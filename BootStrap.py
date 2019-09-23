import subprocess
import time
from os import system, name 
from threading import Thread
import sys

def Core_Compute():
  subprocess.run("terminator --new-tab -e 'python3 /home/badboy17g/HackoHolics/Core_Compute/Core_Compute.py'", shell=True)

def Hotword():
  subprocess.run("terminator --new-tab --working-directory='/home/badboy17g/HackoHolics/Hotword' -e 'python3 /home/badboy17g/HackoHolics/Hotword/Hotword.py'", shell=True)

def Module_Loader():
  subprocess.run("terminator --new-tab -e 'python3 /home/badboy17g/HackoHolics/Module_Loader/ModuleLoader.py'", shell=True)

def NLU():
  subprocess.run("terminator --new-tab -e 'python3 /home/badboy17g/HackoHolics/NLU/NLU.py'", shell=True)

def Special_Functions():
  subprocess.run("terminator --new-tab -e 'python3 /home/badboy17g/HackoHolics/Special_Functions/Function_Handler.py'", shell=True)

def Voice():
  subprocess.run("terminator --new-tab -e 'python3 /home/badboy17g/HackoHolics/Voice/Audio.py'", shell=True)
# /home/badboy17g/HackoHolics/Object_detection/Object detection.py

def Objects_detect():
  subprocess.run("terminator --new-tab -e 'python3 /home/badboy17g/HackoHolics/Object_detection/Object_detection.py'", shell=True)
# /home/badboy17g/HackoHolics/Vision_Mod/Current_User/User_Recoginition.py
def Current_User():
  subprocess.run("terminator --new-tab -e 'python3 /home/badboy17g/HackoHolics/Vision_Mod/Current_User/User_Recoginition.py'", shell=True)

# /home/badboy17g/HackoHolics/Vision_Mod/Neural_Mindset/Current_Vision_State.py
def Current_Vision():
  subprocess.run("terminator --new-tab -e 'python3 /home/badboy17g/HackoHolics/Vision_Mod/Neural_Mindset/Current_Vision_State.py'", shell=True)


if __name__ == "__main__":
    
    Core_Compute = Thread(target = Core_Compute)
    Hotword = Thread(target = Hotword)
    Module_Loader = Thread(target = Module_Loader)
    NLU = Thread(target = NLU)
    Special_Functions = Thread(target = Special_Functions)
    Voice = Thread(target = Voice)
    Objects_detect = Thread(target = Objects_detect) 
    Current_User = Thread(target= Current_User)
    Current_Vision = Thread(target = Current_Vision)

    Core_Compute.start()
    time.sleep(10)
    Hotword.start()
    Module_Loader.start()
    NLU.start()
    Special_Functions.start()
    Voice.start()
    Objects_detect.start()
    Current_User.start()
    Current_Vision.start()
   
    Core_Compute.join()
    Hotword.join()
    Module_Loader.join()
    NLU.join()
    Special_Functions.join()
    Voice.join()
    Objects_detect.join()
    Current_User.join()
    Current_Vision.join()
    

