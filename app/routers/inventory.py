from fastapi import APIRouter, status, HTTPException
import json
from ..models.inventroy_schemas import Inventory, InventoryUpdate
from ..models.validateDB import validateDB

router = APIRouter(
    prefix="/inventory", tags=["inventory"]
)


@router.get("/", status_code=status.HTTP_200_OK)
async def read_inventory():
    with open("app/documents/inventory_db.json", "r", encoding="utf-8") as file:
        inventory_db = json.load(file)
        inventory_db = validateDB(inventory_db, "inventory")
        print(inventory_db)
        return {
            "success": True,
            "data": inventory_db
        }
        
@router.get("/{intentoryItemID}", status_code=status.HTTP_200_OK)
async def get_inventory_item_by_id(intentoryItemID: str):
    with open("app/documents/inventory_db.json", "r",encoding="utf-8") as file:
        inventory_db = json.load(file)
        inventory_db = validateDB(inventory_db, "inventory")
    
    filteredItem = {inventoryKey: inventoryValue for inventoryKey, inventoryValue in inventory_db.items() if inventoryKey == intentoryItemID}
        
    if filteredItem == {}:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    else:      
        
        return {"success": True,
                "data": filteredItem}
        
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_inventory_item(inventoryItemID: str, itemData: Inventory):
    with open("app/documents/inventory_db.json", "r", encoding="utf-8") as file:
        inventory_db = json.load(file)
        inventory_db = validateDB(inventory_db, "inventory")
        # Si el animal ya existe en la base de datos no hace nada
        for inventoryKey in inventory_db.keys():
            if inventoryKey.lower() == inventoryItemID.lower():
                return {"message": "Item already exists."}
            
        newInventoryItem = {inventoryItemID: itemData.model_dump()}
        inventory_db.update(newInventoryItem)
        print(inventory_db)
        
        with open("app/documents/inventory_db.json", "w", encoding="utf-8") as file:
            json.dump(inventory_db, file)
        
        return {
            "success": True,
            "data": newInventoryItem,
        }
        
@router.delete("/{inventoryItemID}", status_code=status.HTTP_204_NO_CONTENT)
async def detele_inventory_item(inventoryItemID: str):
    with open("app/documents/inventory_db.json", "r",encoding="utf-8") as file:
        inventory_db = json.load(file)
        inventory_db = validateDB(inventory_db, "inventory")
        
    if inventoryItemID not in inventory_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    del inventory_db[inventoryItemID]
        
    with open("app/documents/inventory_db.json", "w", encoding="utf-8") as file:
        json.dump(inventory_db, file)
        
@router.put("/{inventoryItemID}", status_code=status.HTTP_200_OK)
async def modify_inventory_item(inventoryItemID: str, modifyData: InventoryUpdate):
    with open("app/documents/inventory_db.json", "r",encoding="utf-8") as file:
        inventory_db = json.load(file)
        inventory_db = validateDB(inventory_db, "inventory")
        
        if inventoryItemID not in inventory_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        
    modifyDataDict = modifyData.model_dump(exclude_unset=True)     
    inventory_db[inventoryItemID].update(modifyDataDict)
    
    with open("app/documents/inventory_db.json", "w", encoding="utf-8") as file:
        json.dump(inventory_db, file)
    
    return{
        "success": True,
        "data": "Item updated correctly"
    }