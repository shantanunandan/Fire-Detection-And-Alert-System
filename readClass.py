
import datetime

class readClass:
	status = ""
	def sensorStatus(self):
		if fire.v == 1:
			return 1

	def readStatus(self,filename):
		try:
			f = open(filename,"r")
			content = f.read()
			self.status=content
			return content
		except:
			f = open(filename,"r")
			content = f.read()
			self.status=content
			return content
		finally:
			f.close()

	def clearing(self):
		try:
			f1 = open("temp.txt","w")
			f1.write(self.status)

			f2 = open("motion.txt","w")
			f2.write(self.status)

			f3 = open("gas.txt","w")
			f3.write(self.status)

			f4 = open("fire.txt","w")
			f4.write(self.status)
		except:
			f1 = open("temp.txt","w")
			f1.write(self.status)

			f2 = open("motion.txt","w")

			f3 = open("gas.txt","w")
			f3.write(self.status)

			f4 = open("fire.txt","w")
			f4.write(self.status)
		finally:
			f1.close()
			f2.close()
			f3.close()
			f4.close()
		

