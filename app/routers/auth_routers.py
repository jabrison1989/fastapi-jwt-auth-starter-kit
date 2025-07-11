from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from app.models.auth_models import Account
from app.schemas.user import AccountCreate, AccountLogin, AccountResponse
from app.services.auth_services import register_user, login_user
from app.dependencies import get_db, get_current_user

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/register", response_model=AccountResponse)
def register(user: AccountCreate, db: db_dependency):
    return register_user(user, db)

@router.post("/login")
def login(user: AccountLogin, db: db_dependency):
    return login_user(user, db)

@router.get("/me")
def get_profile(user: Account = Depends(get_current_user)):
    return user