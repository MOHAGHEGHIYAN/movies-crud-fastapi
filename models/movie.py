from pydantic import BaseModel


class Movie(BaseModel):
    title: str
    genres: str
