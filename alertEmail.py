import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
class email:
	def emailSend(self,name,path,temp,motion,fire):
		fromaddr = "fier@gmail.com"
		toaddr = "abcd@gmail.com" 
		msg = MIMEMultipart()
 
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Fire Broke Out. Please Respond."
 
		body = "Address :  Put Address\n"+"Temprature : "+temp+"\n"+"Life Pregence : "+motion+"\n"+"Active Fire : "+fire+"\n"
 
		msg.attach(MIMEText(body, 'plain'))

		filename = name
		path = path
		attachment = open(path , "rb")
 
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
		msg.attach(part)
 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, "123456")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		print("Mail Send")

	def emailGas(self,name,path):
		fromaddr = "fier@gmail.com"
		toaddr = "abcd@gmail.com" 
		msg = MIMEMultipart()
 
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Fire Broke Out. Please Respond."
 
		body = "Address : Put Address\n"+"Gas Leakage Is Reported Here"
 
		msg.attach(MIMEText(body, 'plain'))
 
		filename = name
		path = path
		attachment = open(path , "rb")
 
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
		msg.attach(part)
 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, "123456")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		print("Mail Send")


