from pydantic import BaseModel


class BookModel(BaseModel):
    """ 
       this class model validates the data type 
       of the input fields(entered by user) to ensure 
       its consistent with the data type of the fields 
       in the database table (i.e. the Book class in models.py) 
    """
    title: str
    author: str
    year: int
    isbn: str


class BookModelWithId(BookModel):
    """ 
       this class model is a child of the BookModel,
       only used when the book ID is required.
       it was created because the book ID is auto-generated
       (book ID is not an input field) 
    """
    id: int

    class Config:
        orm_mode = True