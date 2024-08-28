from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import Union
import os

router = APIRouter()

@router.get("/test")
def test_image_processing():
    return {"message": "This is a test endpoint for image processing."}

@router.post("/upload")
async def upload_single_image(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    # Define the path where the file will be saved
    upload_folder = "app/static/uploads/"
    os.makedirs(upload_folder, exist_ok=True)
    
    file_path = os.path.join(upload_folder, file.filename)
    
    try:
        # Save the uploaded file to the specified path
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")
    
    return {"filename": file.filename, "message": "File successfully uploaded"}

@router.get("/download/{filename}")
async def download_image(filename: str):
    # Define the path where the files are stored
    upload_folder = "app/static/uploads/"
    file_path = os.path.join(upload_folder, filename)
    
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    # Return the file as a response
    return FileResponse(file_path, media_type='image/jpeg')