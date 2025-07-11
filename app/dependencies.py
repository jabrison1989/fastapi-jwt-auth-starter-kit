from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError
from app.services.token import verify_token
from app.services.database import SessionLocal
from app.models.auth_models import Account

oauth2_scheme = HTTPBearer()

def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

def get_current_user(token: HTTPAuthorizationCredentials = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Account:
    email = verify_token(token.credentials)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user = db.query(Account).filter(Account.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

