from pydantic import BaseModel

class Animal(BaseModel):
        species: str
        habitat: str
        diet : list[str]
        lifespan: int
        
        
class AnimalUpdate(BaseModel):
        species: str | None = None
        habitat: str | None = None
        diet : list[str] | None = None
        lifespan: int | None = None