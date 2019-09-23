from nanpy import SerialManager
connection = SerialManager(device='/dev/ttyACM0')
from nanpy import ArduinoApi
a = ArduinoApi(connection=connection)
a.pinMode(12, a.OUTPUT)
a.digitalWrite(12, a.LOW)
