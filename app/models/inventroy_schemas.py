from pydantic import BaseModel

class Inventory(BaseModel):
    name: str
    category: str
    quantity: int
    location: str
    condition: str | None = None
    last_maintenance: str
    description: str | None = None
    
    
    
class InventoryUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    quantity: int | None = None
    location: str | None = None
    condition: str | None = None
    last_maintenance: str | None = None
    description: str | None = None    