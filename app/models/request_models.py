from pydantic import BaseModel

class ImageProcessingRequest(BaseModel):
    image_path: str
    clip_limit: float = 2.0
    tile_size: tuple = (8, 8)
