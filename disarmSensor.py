#!/usr/bin/env python
import RPi.GPIO as GPIO
import led
import time
import commandCenter

class disarmSensor:
	def __init__(self):
		led.led().ledOff(29)
		led.led().ledOff(31)
		led.led().ledOff(33)
		led.led().ledOff(40)
		GPIO.cleanup()		

disarmSensor()

