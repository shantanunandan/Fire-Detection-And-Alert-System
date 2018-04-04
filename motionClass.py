import RPi.GPIO as GPIO                           
import time                                       
import led

class motion:
	sensorStatus = "2"
	def setstatus(self):
		try:
			f = open("motion.txt","w")
			f.write(self.sensorStatus)
		except:
			f = open("motion.txt","w")
			f.write(self.sensorStatus)
		finally:
			f.close()
			
	def __init__(self,pir,red,green):
		GPIO.setmode(GPIO.BOARD)                          
		self.flag = 0                                     
		GPIO.setup(pir, GPIO.IN)                           
		print ("Waiting for sensor to settle")
		time.sleep(2)                                     
		print ("Detecting motion")
		l = led.led()
		for i in range(0,10):
			if GPIO.input(pir):                            
				print ("Motion Detected!")
				self.flag = 1
				self.sensorStatus = "motion1"
				self.setstatus()                           
				print("\nPassing control to GAS Sensor")
				break
			time.sleep(0.1)                                
