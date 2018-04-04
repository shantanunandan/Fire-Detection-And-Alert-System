#!/usr/bin/env python
import RPi.GPIO as GPIO
import led
import time
import commandCenter

class armSensor:
	def __init__(self):
		led.led().ledOn(29)
		commandCenter.fire(36).run()
