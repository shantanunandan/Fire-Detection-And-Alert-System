from twilio.rest import Client

class sms:
	def __init__(self,toNum):
		# Your Account SID from twilio.com/console
		account_sid = "Put Twilio Account SID"
		# Your Auth Token from twilio.com/console
		auth_token  = "Put Twilio Account auth_token"

		client = Client(account_sid, auth_token)

		message = client.messages.create(
    			to=toNum, 
    			from_="Put number generated by twilio",
    			body="Your message body")

		print(message.sid)

