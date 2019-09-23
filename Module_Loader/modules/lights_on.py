from nanpy import SerialManager
import time
connection = SerialManager(device='/dev/ttyACM0')
from nanpy import ArduinoApi
a = ArduinoApi(connection=connection)
a.pinMode(12, a.OUTPUT)
a.digitalWrite(12, a.HIGH)
time.sleep(5)
