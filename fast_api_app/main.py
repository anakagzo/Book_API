from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Book, Base
from schemas import BookModel, BookModelWithId


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  


@app.get('/books/',response_model=list[BookModelWithId])
def retrieve_all_books(db: Session = Depends(get_db)):
    """ 
       this function returns the list of books in the database
    """
    books = db.query(Book).all()
    return books


@app.get('/books/{id}',response_model=BookModelWithId)
def retrieve_book(id: int, db: Session = Depends(get_db)):
    """ 
       this function returns a particular book information based 
       on ID provided
    """
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise HTTPException(status_code=404,detail='item not found')
    return book


@app.post('/books/',response_model=None, status_code=status.HTTP_201_CREATED)
def add_book(book: BookModel, db: Session = Depends(get_db)):
    """ 
       this function adds a new book record to the database and returns
       201 status code
    """
    db_book = Book(title=book.title, author=book.author,
                   year=book.year, isbn=book.isbn)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return status.HTTP_201_CREATED


@app.put('/books/{id}',response_model=None, status_code=status.HTTP_200_OK)
def update_book(id: int, book: BookModel, db: Session = Depends(get_db)):
    """ 
       this function updates the information of a particular book 
       according to the provided ID in the database and returns 
       200 status code
    """
    book_to_update = db.query(Book).filter(Book.id == id).first()
    if book_to_update is None:
        raise HTTPException(status_code=404,detail='item not found')
    
    book_to_update.title = book.title
    book_to_update.author = book.author
    book_to_update.year = book.year
    book_to_update.isbn = book.isbn
    db.commit()
    return status.HTTP_200_OK


@app.delete('/books/{id}', response_model=None, status_code=status.HTTP_200_OK)
def delete_book(id: int, db: Session = Depends(get_db)):
    """ 
       this function deletes a book record from the database 
       according to the provided ID and returns 200 status code
    """
    book_to_delete = db.query(Book).filter(Book.id == id).first()
    if book_to_delete is None:
        raise HTTPException(status_code=404,detail='item not found')
    
    db.delete(book_to_delete)
    db.commit()
    return status.HTTP_200_OK