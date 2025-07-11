from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.database import Base, engine
from app.routers import auth_routers  # <- this imports your APIRouter

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI AuthService",
    version="1.0.0",
    description="Plug-and-play JWT authentication service for solo devs and indie projects."
)

# CORS middleware (for frontend/backend separation)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to specific domains in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your modular router
app.include_router(auth_routers.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "FastAPI AuthService is running"}
