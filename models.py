from typing import Any, Generic, List, Optional, TypeVar
from pydantic import BaseModel
from pydantic.generics import GenericModel

DataType = TypeVar("DataType")

class IResponseBase(GenericModel, Generic[DataType]):
    message: str = ""
    status : str = ""
    items  : Optional[DataType] = None


class Employee(BaseModel) :
   empName : str
   location :str
   designation :str
   experience :int
   contactno : int
   password :str
   email : str
   access : str

class showemployees(BaseModel):
   empName : str
   location :str
   designation :str
   experience :int
   contactno : int
   email : str
   class Config():
    orm_mode = True 
   