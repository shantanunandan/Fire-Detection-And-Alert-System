import os
import time
import buzzer

class cam:
	def __init__(self,name):
		cmd = 'fswebcam --no-banner -S 20 -q -r 640x480 '+name+'.png'
		for i in range(0,10):
			try:
				time.sleep(1)
				os.system(cmd)
			except:
				time.sleep(1)
				os.system(cmd)
