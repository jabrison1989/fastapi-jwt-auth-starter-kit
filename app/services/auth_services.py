from app.schemas.user import AccountCreate, AccountLogin
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.auth_models import Account
from app.services.token import create_access_token
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    """Hashes a password using bcrypt (used by Everblade Online)."""
    return pwd_context.hash(password)

def register_user(user: AccountCreate, db: Session):
    """Registers a new account in the auth database."""
    user_data = user.model_dump()
    user_data['password'] = hash_password(user_data['password'])

    new_user = Account(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(user: AccountLogin, db: Session):
    db_user = db.query(Account).filter(Account.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(subject=db_user.email)
    return {"access_token": token, "token_type": "bearer"}
