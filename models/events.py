from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str   # 이미지 경로
    description: str
    tags: List[str]
    location: str
    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Study",
                "image" : "https://www.test.pri/image.png",
                "description": "간단한 설명을 추가하세요",
                "tags": ["python", "fastapi", "study"],
                "location": "Google Meet"
        }
    }