from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Sample FastAPI Project",
    description="Simple FastAPI CRUD example",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Hello Welcome to FastAPI 🚀"}

# To add heatlh check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}
# to add status endpoint
@app.get("/status")
def status():
    return {"status": "running"}