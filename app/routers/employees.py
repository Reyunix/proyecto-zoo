from fastapi import APIRouter, status, HTTPException
import json
from ..models.employees_schemas import Employee, EmployeeUpdate
from ..models.validateDB import validateDB

router = APIRouter( prefix="/employees", tags=["Employees"])


@router.get("/", status_code=status.HTTP_200_OK)
async def read_employees():
    with open("app/documents/employees_db.json", "r", encoding="utf-8") as file:
        employees_db = json.load(file)
        employees_db = validateDB(employees_db, "employee")
        print(employees_db)
        return {
            "success": True,
            "data": employees_db
        }
        
@router.get("/{employeeID}", status_code=status.HTTP_200_OK)
async def get_employee_by_id(employeeID: str):
    with open("app/documents/employees_db.json", "r",encoding="utf-8") as file:
        employees_db = json.load(file)
        employees_db = validateDB(employees_db, "employee")
    
    filteredEmployee = {employeeKey: employeeValue for employeeKey, employeeValue in employees_db.items() if employeeKey == employeeID}
        
    if filteredEmployee == {}:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    else:
        
        
        return {"success": True,
                "data": filteredEmployee}
        
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_employee(employeeID: str, employeeData: Employee):
    with open("app/documents/employees_db.json", "r", encoding="utf-8") as file:
        employees_db = json.load(file)
        employees_db = validateDB(employees_db, "employee")
        # Si el animal ya existe en la base de datos no hace nada
        for employeeKey in employees_db.keys():
            if employeeKey.lower() == employeeID.lower():
                return {"message": "Employee already exists."}
            
        newEmployee = {employeeID: employeeData.model_dump()}
        employees_db.update(newEmployee)
        print(employees_db)
        
        with open("app/documents/employees_db.json", "w", encoding="utf-8") as file:
            json.dump(employees_db, file)
        
        return {
            "success": True,
            "data": newEmployee,
        }
        
@router.delete("/{employeeID}", status_code=status.HTTP_204_NO_CONTENT)
async def detele_employee(employeeID: str):
    with open("app/documents/employees_db.json", "r",encoding="utf-8") as file:
        employees_db = json.load(file)
        employees_db = validateDB(employees_db, "employee")
        
    if employeeID not in employees_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

    del employees_db[employeeID]
        
    with open("app/documents/employees_db.json", "w", encoding="utf-8") as file:
        json.dump(employees_db, file)
        
@router.put("/{employeeID}", status_code=status.HTTP_200_OK)
async def modify_employee(employeeID: str, modifyData: EmployeeUpdate):
    with open("app/documents/employees_db.json", "r",encoding="utf-8") as file:
        employees_db = json.load(file)
        employees_db = validateDB(employees_db, "employee")
        
        if employeeID not in employees_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
        
    modifyDataDict = modifyData.model_dump(exclude_unset=True)     
    employees_db[employeeID].update(modifyDataDict)
    
    with open("app/documents/employees_db.json", "w", encoding="utf-8") as file:
        json.dump(employees_db, file)
    
    return{
        "success": True,
        "data": "Employee updated correctly"
    }