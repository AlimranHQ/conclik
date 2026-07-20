from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, profile

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ContentPilot AI",
    version="2.0.0"
)

app.include_router(auth.router)
app.include_router(profile.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to ContentPilot AI API 🚀"
    }
