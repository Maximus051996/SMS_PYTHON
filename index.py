from fastapi import Depends, FastAPI
import dbschema
from db import *
from models import Employee 
# from twilio.rest import Client
from routers import emp_router

app=FastAPI()


dbschema.Base.metadata.create_all(engine)

app.include_router(emp_router.router)


# @app.post('/sendnotificationwp',tags=["Email"])
# async def sendnotification(body:str,to:str) :
#     try:       
#         account_sid ='AC80e595396e51ad023a0a2dffd3ff6298'
#         auth_token='ed428e0f178385b2797e920b99931f4a'
#         twilio_number='+14155238886'
#         client = Client(account_sid, auth_token)
#         message = client.messages.create(
#             body=body,
#             from_='whatsapp:' + twilio_number,
#             to='whatsapp:' + to
#         )
#         return {'message': 'Message sent successfully.', 'message_sid': message.sid}
#     except Exception as e:
#         return {'message': 'Failed to send message.', 'error': str(e)}



