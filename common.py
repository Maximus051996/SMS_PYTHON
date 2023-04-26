from enum import Enum
from db import SessionLocal


def get_db() :
    db=SessionLocal()
    try :
       yield db
    finally:
        db.close()

class MessageType(Enum):
    ERROR   = "Error occurred, Please try again !!"
    Success = "Data created sucessfully !!"      
    Update  = "Data updated sucessfully !!"
    Delete  = "Data deleted sucessfully !!"
    Fetch  =  "Data getting sucessfully !!"
    Missing = "Data not Found !!"

class AccessType(Enum):
    SA   = "Super Admin"
    ADM  = "Admin"
    SUV  = "Supervisor"
    SG   = "Agent"
    CUST = "Customer"

    