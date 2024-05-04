from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    year: int
    isbn: str

class BookWithId(BookBase):
    id: int

    class Config:
        orm_mode = True