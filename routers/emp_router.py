from typing import List
from fastapi import APIRouter, Depends
from common import MessageType, get_db
from db import *
from models import * 
from sqlalchemy.orm import Session
from Repository import EmpRepos

router = APIRouter(
   tags=["Users"]
)

# Employee Module

@router.get('/getEmployees',response_model=IResponseBase[List[showemployees]])
async def getEmployees(dbcon: Session = Depends(get_db)) :
  return EmpRepos.get_all_Employees(dbcon)

@router.get('/getEmployeeById',response_model=IResponseBase[showemployees])
async def getEmployeeById(empId : int,dbcon: Session = Depends(get_db)) :
  return EmpRepos.getemployeeById(dbcon,empId)

@router.post('/insertEmployee',response_model=IResponseBase[Employee])
async def createEmployee(employeeobj : Employee ,dbcon: Session = Depends(get_db)) -> Employee :
  return EmpRepos.insertemployee(dbcon,employeeobj)

@router.delete('/deleteEmployee',response_model=IResponseBase[Employee])
async def deleteEmployee(employeeid : int ,dbcon: Session = Depends(get_db))  -> Employee :
  return EmpRepos.deleteemployee(dbcon,employeeid)


@router.post('/updateEmployee',response_model=IResponseBase[Employee])
async def updateEmployee(empId:int ,location :str ,designation :str ,contactno :int,
                   experience :int,email :str,
                   dbcon: Session = Depends(get_db)) :
   return EmpRepos.updateemployee(dbcon,empId,location,designation,contactno,experience,email)