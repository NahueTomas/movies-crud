from typing import Optional
from pydantic import BaseModel

# Types
from models.movie import Title, Release, Rated, Image


class MovieCreate(BaseModel):
    title: Title
    release: Release
    rated: Rated = 'N/A'
    image: Image = ""


class MoviePut(BaseModel):
    title: Optional[Title]
    release: Optional[Release]
    rated: Optional[Rated]
    image: Optional[Image]
