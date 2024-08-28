from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_image_processing():
    return {"message": "This is a test endpoint for image processing."}
