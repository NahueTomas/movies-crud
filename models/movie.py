from dataclasses import dataclass
from typing import Literal

from uuid import UUID

Id = UUID
Title = str
Release = str
Rated = Literal['G', 'PG', 'PG-13', 'R', 'NC-17', 'TV-MA', 'TV-14', 'N/A']
Image = str


@dataclass
class Movie:
    id: Id
    title: Title
    release: Release
    rated: Rated = "N/A"
    image: Image = ""
