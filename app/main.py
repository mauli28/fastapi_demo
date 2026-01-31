
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.routes import router


app = FastAPI(
    title="Sample FastAPI Project",
    description="Simple FastAPI CRUD example",
    version="1.0.0"
)

# Mount static directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(router)


# Serve index.html at root
@app.get("/", include_in_schema=False)
async def root():
    return FileResponse("app/static/index.html")

# To add heatlh check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}
# to add status endpoint
@app.get("/status")
def status():
    return {"status": "running"}