from typing import Union, List, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for personnel data (replace with a database in production)
personnel_db = []

# Pydantic model for personnel data
class Personnel(BaseModel):
    name: str
    email: str
    role: str
    sap_access_level: str  # e.g., "Read", "Write", "Admin"

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Project e-Delta Personnel Management API"}

# Endpoint to create a new personnel record
@app.post("/personnel/", response_model=Personnel)
def create_personnel(personnel: Personnel):
    personnel_db.append(personnel.dict())
    return personnel

# Endpoint to retrieve all personnel records
@app.get("/personnel/", response_model=List[Personnel])
def get_all_personnel():
    return personnel_db

# Endpoint to retrieve a specific personnel record by email
@app.get("/personnel/{email}", response_model=Personnel)
def get_personnel_by_email(email: str):
    for person in personnel_db:
        if person["email"] == email:
            return person
    raise HTTPException(status_code=404, detail="Personnel not found")

# Endpoint to update a personnel record by email
@app.put("/personnel/{email}", response_model=Personnel)
def update_personnel(email: str, updated_personnel: Personnel):
    for idx, person in enumerate(personnel_db):
        if person["email"] == email:
            personnel_db[idx] = updated_personnel.dict()
            return updated_personnel
    raise HTTPException(status_code=404, detail="Personnel not found")

# Endpoint to delete a personnel record by email
@app.delete("/personnel/{email}", response_model=Dict[str, str])
def delete_personnel(email: str):
    for idx, person in enumerate(personnel_db):
        if person["email"] == email:
            del personnel_db[idx]
            return {"message": "Personnel deleted successfully"}
    raise HTTPException(status_code=404, detail="Personnel not found")