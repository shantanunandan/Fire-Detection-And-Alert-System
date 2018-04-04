import RPi.GPIO as GPIO
import time

class led:
	def run(self,pin,delay):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin,GPIO.OUT)
		GPIO.setwarnings(False)
		for i in range(0,4):
			time.sleep(1)
			GPIO.output(pin,0)
			time.sleep(delay)
			GPIO.output(pin,1)
			time.sleep(delay)
			GPIO.output(pin,0)

	def ledOff(self,pin):
                GPIO.setwarnings(False)
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(pin,GPIO.OUT)
                GPIO.setwarnings(False)
                GPIO.output(pin,0)

	def ledOn(self,pin):
                GPIO.setwarnings(False)
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(pin,GPIO.OUT)
                GPIO.setwarnings(False)
                GPIO.output(pin,1)

#l = led()
#l.run(29,0.2)			

