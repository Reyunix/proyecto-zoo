from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    age : int
    position: str
    salary: int | None = None
    department: str
    location: str
    
class EmployeeUpdate(BaseModel):
    name: str | None = None
    age : int | None = None
    position: str | None = None
    salary: int | None = None
    department: str | None = None
    location: str | None = None