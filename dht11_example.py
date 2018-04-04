import RPi.GPIO as GPIO
import dht11
import time
import datetime
from led import led

class temprature:
	sensorStatus = "2"
	def setstatus(self):
		try:
			f = open("temp.txt","w")
			f.write(self.sensorStatus)
		except:
			f = open("temp.txt","w")
			f.write(self.sensorStatus)
		finally:
			f.close()
	def __init__(self):
		# initialize GPIO
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)

		# read data using pin 12
		self.instance = dht11.DHT11(pin=12)
		i = 0
		try:		
			self.result = self.instance.read()
			if self.result.is_valid() > 40:
				self.sensorStatus = "temprature1"
				self.setstatus()
				print("Temprature : ",self.setstatus()) 
				print("\nPassing control to Motion Sensor to detect presence of life")
			else:
                                print("Temprature : ",self.setstatus()) 
		except KeyboardInterrupt:
			print("Ctrl-C - quit")
