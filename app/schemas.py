from typing import List
from pydantic import BaseModel


class AlbumBase(BaseModel):
    title: str
    artist: str
    genre_id: int
    user_id: int


class AlbumCreate(AlbumBase):
    pass


class Album(AlbumBase):
    id: int

    class Config:
        orm_mode = True


class AlbumUpdate(BaseModel):
    title: str = None
    artist: str = None
    user_id: int = None
    genre_id: int = None


class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    pass


class Genre(GenreBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    albums: list[Album] = []

    class Config:
        orm_mode = True
