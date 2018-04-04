import time, sys
import RPi.GPIO as GPIO
import datetime
from alertEmail import email

class gas:
	sensorStatus = "2"
	def setstatus(self):
		try:
			f = open("gas.txt","w")
			f.write(self.sensorStatus)
		except:
			f = open("gas.txt","w")
			f.write(self.sensorStatus)
			print("Except : ",self.sensorStatus)
		finally:
			f.close()

	def __init__(self,pin):
		self.gpin = pin
		self.LeakStatus = 1
		print("Arming gas sensor to detect gas leakage") 
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.gpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	def myISR(self,ev=None):
		v = GPIO.input(self.gpin)
		print("V : ",v)
		while v==0:
			self.LeakStatus = 0
			self.sensorStatus = "gas1"
			self.setstatus()
			print ("Gas leakage is detected !")
			print (str(datetime.datetime.now()))
			email().emailGas("fire.png","/home/pi/project/fire.png")
			print("Passing control to Flame Sensor")
			return

	def loop(self):
		v = GPIO.input(self.gpin)
		print("Loop :",self.LeakStatus)
		GPIO.add_event_detect(self.gpin, GPIO.RISING, callback=self.myISR)
		i = 0
		for i in range(0,9999999):
			if self.LeakStatus == 0:
				return
			pass

	def grun(self):
		try:
			self.loop()
		except KeyboardInterrupt: 
			print ("The end !")
			print(self.LeakStatus)
