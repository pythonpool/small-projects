from twilio.rest import Client

account_sid = 'AC0f8d2de08d5514d34a1b4ac88e4acd4b'
auth_token = '95e7b4eeddb21d1e9a1798ddb86b73b7'
client = Client(account_sid, auth_token)

message = client.messages.create(
         media_url=["https://www.qsrmagazine.com/sites/default/files/story/red-roofs-are-haunting-pizza-huts-sales.jpg"],
         from_='whatsapp:+14155238886',
         body="Let's have pizza buddy!",
         to='whatsapp:+919540909248'
     )

print(message.sid)