from pydantic import BaseModel, EmailStr
from datetime import datetime

class AccountCreate(BaseModel):
    email: EmailStr
    password: str

class AccountLogin(BaseModel):
    email: EmailStr
    password: str

class AccountResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
