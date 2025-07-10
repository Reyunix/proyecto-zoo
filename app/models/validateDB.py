from pydantic import ValidationError
from app.models.animals_schemas import Animal
from app.models.employees_schemas import Employee
from app.models.inventroy_schemas import Inventory

def validateDB(dbFile: dict, schema: str):
    validatedDict = {}
        
    for dbKey, dbValue in dbFile.items():
        try:  # Intenta la validación con la clase Animal y actualiza el diccionario vacío. Si falla no hace nada
            if schema == "animal":
                validatedData = Animal(
                                species = dbValue["species"],
                                habitat = dbValue["habitat"],
                                diet = dbValue["diet"],
                                lifespan = dbValue["lifespan"]
                ).model_dump()

                validatedDict.update({dbKey: validatedData})
            if schema == "employee":
                validatedData = Employee(
                                name = dbValue["name"],
                                age = dbValue["age"],
                                position = dbValue["position"],
                                salary = dbValue["salary"],
                                department = dbValue["department"],
                                location = dbValue["location"]
                ).model_dump()

                validatedDict.update({dbKey: validatedData})
            if schema == "inventory":
                validatedData = Inventory(
                                name = dbValue["name"],
                                category = dbValue["category"],
                                quantity = dbValue["quantity"],
                                location = dbValue["location"],
                                condition = dbValue["condition"],
                                last_maintenance = dbValue["last_maintenance"],
                                description = dbValue["description"]
                ).model_dump()
                
                validatedDict.update({dbKey:validatedData})
                
                
        except ValidationError:
            pass
    return validatedDict