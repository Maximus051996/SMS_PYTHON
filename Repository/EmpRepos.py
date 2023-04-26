from typing import List
from sqlalchemy.orm import Session
from common import *
import dbschema
from fastapi import  HTTPException
from sqlalchemy.exc import SQLAlchemyError
from models import *
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_all_Employees(dbcon:Session) :
 try :
  items = dbcon.query(dbschema.Employee).all()
  result_set= [showemployees(empName=e.empName, location=e.location,
                            designation=e.designation,experience=e.experience,
                            contactno=e.contactno,email=e.email) for e in items] 
  return IResponseBase[List[showemployees]](items=result_set,
          message=MessageType.Fetch.value,status=MessageType.Fetch.name)
 except Exception as e :
    print(e)
    raise HTTPException(status_code=500,detail=MessageType.ERROR.value)
 finally:
        dbcon.close() 

def getemployeeById(dbcon : Session , employeeid : any) :
 try :
      record = dbcon.query(dbschema.Employee).filter_by(id=employeeid).first()
      if not record :
       raise HTTPException(status_code=500,detail=MessageType.Missing.value)
      return IResponseBase[showemployees](items=record,
          message=MessageType.Fetch.value,status=MessageType.Fetch.name)
 except SQLAlchemyError as e :
      raise HTTPException(status_code=500,detail=MessageType.ERROR.value)
 finally:
        dbcon.close() 

def insertemployee(dbcon : Session,employeeobj : any) :
 try :
      record_data = dbschema.Employee(
      empName=employeeobj.empName,
      location=employeeobj.location,
      designation=employeeobj.designation,
      experience=employeeobj.experience,
      contactno=employeeobj.contactno,
      password=pwd_context.hash(employeeobj.password),
      email=employeeobj.email,
      access=employeeobj.access
      )
      dbcon.add(record_data)
      dbcon.commit()
      return IResponseBase[Employee](message=MessageType.Success.value
      ,status=MessageType.Success.name)
 except Exception as e :
      raise HTTPException(status_code=500,detail=MessageType.ERROR.value)
 finally:
        dbcon.close()

def deleteemployee(dbcon :Session ,employeeid : any) :
 try :
    record = dbcon.query(dbschema.Employee).filter(dbschema.Employee.id == employeeid).first()
    if not record :
     raise HTTPException(status_code=500,detail=MessageType.Missing.value)
    dbcon.delete(record)
    dbcon.commit()
    dbcon.flush()
    return IResponseBase[Employee](message=MessageType.Delete.value
      ,status=MessageType.Delete.name)
 except SQLAlchemyError as e:
    dbcon.rollback()
    raise HTTPException(status_code=500, detail=MessageType.ERROR.value)
 finally:
        dbcon.close()
     
def updateemployee(dbcon : Session , empId:int ,location :str ,designation :str ,contactno :int,
                   experience :str,email:str) :
 try :
      record = dbcon.query(dbschema.Employee).filter_by(id=empId).first()
      if not record :
       raise HTTPException(status_code=500,detail=MessageType.Missing.value)
      record.location=location
      record.designation=designation
      record.experience=experience
      record.contactno=contactno,
      record.email=email
      dbcon.commit()
      return IResponseBase[Employee](message=MessageType.Update.value
      ,status=MessageType.Update.name)
 except SQLAlchemyError as e :
      raise HTTPException(status_code=500,detail=MessageType.ERROR.value)
 finally:
      dbcon.close() 

