from twilio.rest import Client
import datetime as dt

# Sends SMS using twilio library
def sendSMS(times):
    now = dt.datetime.now()
    timeNow = now.hour + now.minute/60
    for t in times:
        if (t-0.2 <= timeNow <= t+0.2): 
            account_sid = 'AC330aab7232fe1a86c3b093e6d21e3ada' 
            auth_token = 'e6dfd3eee904ffec9a93d007b2b7da6a' 
            client = Client(account_sid, auth_token) 
            message = client.messages.create(  
                                          messaging_service_sid='MG3835204da7ecfc5ab6bafa75f9243466', 
                                          body='Come to pick up your medications',      
                                          to='+420776826242' 
                                      ) 
            print(message.sid)
