from fastapi import FastAPI
from app.api.endpoints import image_processing
import sys 
import os
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

sys.path.append(os.path.abspath("./app/services"))

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,  # Allows cookies to be sent across domains
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Include the image processing endpoints
app.include_router(image_processing.router, prefix="/image-processing")
