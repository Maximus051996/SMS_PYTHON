from sqlalchemy import BigInteger, Column, Integer, String
from db import * 

class Employee(Base) :

   __tablename__ = "employees"
   
   id = Column(Integer, primary_key=True, index=True,autoincrement=True)
   empName =Column(String(200),nullable=False, unique=True)
   location =Column(String(200),nullable=False)
   designation =Column(String(200),nullable=False)
   experience =Column(Integer,nullable=False)
   contactno = Column(BigInteger,nullable=False, unique=True)
   password = Column(String(400),nullable=False)
   email = Column(String(200),nullable=False, unique=True)
   access = Column(String(100),nullable=True)
