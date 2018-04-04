#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import datetime
from dht11_example import temprature
from motionClass import motion
import gasT
from alertEmail import email
import cam
import buzzer
import led
import sms

class fire:
   flag = 0
   sensorStatus = "2"
   def setstatus(self):
       try:
           f = open("fire.txt","w")
           f.write(self.sensorStatus)
       except:
           f = open("fire.txt","w")
           f.write(self.sensorStatus)
       finally:
           f.close()
			
   def __init__(self,FlamePin):
      self.FlamePin = FlamePin
      print("Running")
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(self.FlamePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
      led.led().ledOn(40) 
      buzzer.buzzer().run(7,0.4)
      led.led().ledOff(31)
      led.led().ledOn(33)

   def myISR(self,ev=None):
      flag = 0
      fire = "Active Fire"
      gas="No"
      life="No"
      temp="No"
      self.flag = GPIO.input(self.FlamePin)
      print(GPIO.input(self.FlamePin))
      self.sensorStatus = "fire"+str(GPIO.input(self.FlamePin))
      if self.sensorStatus == "fire1":
         self.setstatus()
         print ("Flame is detected !")
         led.led().ledOff(33)
         led.led().ledOn(31)
         buzzer.buzzer().controllRunOn(7)
         print (str(datetime.datetime.now()))
      print("\nReading TEMPRATURE of affected area")
      temprature()
      time.sleep(2)
      print("\nDetecting Life in affected area")
      if motion(22,40,38).flag == 1:
            life = "Presence of life in the affected area"    
      time.sleep(2)
      time.sleep(2)
      flag = flag+1
      cam.cam("fire")
      if flag != 0:
           email().emailSend("fire.png","/home/pi/project/fire.png",temp,life,fire)
           print("Mail Sended")
           sms.sms("Number to send")		   
           flag = 0     
      print("Detecting LPG lekage in area")
      gasT.gas(38).grun()
      buzzer.buzzer().controllRunOff(7)


   def loop(self):
      print(GPIO.input(self.FlamePin))
      GPIO.add_event_detect(self.FlamePin, GPIO.FALLING, callback=self.myISR)
      for i in range(0,999999):
          pass
   def run(self):
      try:
         self.loop()
      except KeyboardInterrupt:  
         print ("The end !")
