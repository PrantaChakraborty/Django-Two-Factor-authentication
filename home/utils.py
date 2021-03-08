from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC691f7970c1f19d787fda8672edc75e5c"
auth_token = "e72fa14fec8e60940d02b84c1d302cbf"
client = Client(account_sid, auth_token)

def send_otp(user_code, phone_number):
    message = client.messages.create(
         body=f"Hi, your verification code is {user_code}",
                     from_='+17608405598',
                     to=f"+88{phone_number}"
    )

#print(message.sid)