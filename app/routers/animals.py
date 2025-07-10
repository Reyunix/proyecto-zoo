from fastapi import APIRouter, status, HTTPException
import json
from ..models.animals_schemas import Animal, AnimalUpdate
from ..models.validateDB import validateDB


router = APIRouter( prefix="/animals", tags=["Animals"])



@router.get("/", status_code=status.HTTP_200_OK)
async def read_animals():
    with open("app/documents/animals_db.json", "r", encoding="utf-8") as file:
        animals_db = json.load(file)
        # print(animals_db)
        animals_db = validateDB(animals_db, "animal")
        print(animals_db)
        return {
            "success": True,
            "data": animals_db
        }
        
@router.get("/{animalName}", status_code=status.HTTP_200_OK)
async def get_animal_by_name(animalName: str):
    with open("app/documents/animals_db.json", "r",encoding="utf-8") as file:
        animals_db = json.load(file)
        animals_db = validateDB(animals_db, "animal")

        filteredAnimal = {animalKey: animalValue for animalKey, animalValue in animals_db.items() if animalKey == animalName}
        
        if filteredAnimal == {}:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        else:
            return {"success": True,
                    "data": filteredAnimal}

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_animal(animalName: str, animalData: Animal):
    with open("app/documents/animals_db.json", "r", encoding="utf-8") as file:
        animals_db = json.load(file)
        animals_db = validateDB(animals_db, "animal")
        # Si el animal ya existe en la base de datos no hace nada
        for animalKey in animals_db.keys():
            if animalKey.lower() == animalName.lower():
                return {"message": "Animal already exists."}
            
        newAnimal = {animalName: animalData.model_dump()}
        animals_db.update(newAnimal)
        print(animals_db)
        
        with open("app/documents/animals_db.json", "w", encoding="utf-8") as file:
            json.dump(animals_db, file)
        
        return {
            "success": True,
            "data": newAnimal,
        }

@router.delete("/{animalName}", status_code=status.HTTP_204_NO_CONTENT)
async def detele_animal(animalName: str):
    with open("app/documents/animals_db.json", "r",encoding="utf-8") as file:
        animals_db = json.load(file)
        animals_db = validateDB(animals_db, "animal")
        
    if animalName not in animals_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")

    del animals_db[animalName]
        
    with open("app/documents/animals_db.json", "w", encoding="utf-8") as file:
        json.dump(animals_db, file)

            
@router.put("/{animalName}", status_code=status.HTTP_200_OK)
async def modify_animal(animalName: str, modifyData: AnimalUpdate):
    with open("app/documents/animals_db.json", "r",encoding="utf-8") as file:
        animals_db = json.load(file)
        animals_db = validateDB(animals_db, "animal")
        
        if animalName not in animals_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")
        
    modifyDataDict = modifyData.model_dump(exclude_unset=True)     
    animals_db[animalName].update(modifyDataDict)
    
    with open("app/documents/animals_db.json", "w", encoding="utf-8") as file:
        json.dump(animals_db, file)
    
    return{
        "success": True,
        "data": "Animal updated correctly"
    }