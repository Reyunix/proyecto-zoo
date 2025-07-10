from fastapi import FastAPI
from .routers import animals, inventory, employees

app = FastAPI(
    title="FranAPI"
)   



@app.get("/", tags=["index"])
async def index():
    return {
            "success": True,
            "data": [
                "/animals",
                "/inventory",
                "/employees"
            ],
            "message": "endpoints"
            }
       
app.include_router(animals.router)

app.include_router(inventory.router)

app.include_router(employees.router)




