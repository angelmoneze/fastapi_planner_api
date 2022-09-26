from email.mime import image
from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Titre de l'évènement",
                "image": "https://liendelimage.com/image.png",
                "description": "Description de l'évènement",
                "tags": ["python","fastapi","app","dev"],
                "location": "Google Meet"
            }
        }