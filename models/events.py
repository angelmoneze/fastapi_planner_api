from sqlmodel import JSON, SQLModel, Field, Column
from typing import List, Optional


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "Titre de l'évènement",
                "image": "https://liendelimage.com/image.png",
                "description": "Description de l'évènement",
                "tags": ["python","fastapi","app","dev"],
                "location": "Google Meet"
            }
        }

class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]


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