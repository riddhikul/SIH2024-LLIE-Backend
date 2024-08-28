from fastapi import FastAPI
from app.api.endpoints import image_processing

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Include the image processing endpoints
app.include_router(image_processing.router, prefix="/image-processing")
