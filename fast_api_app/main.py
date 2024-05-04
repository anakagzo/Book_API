from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Book, Base
from schemas import BookBase, BookWithId



Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  


@app.get('/books/',response_model=list[BookWithId])
def retrieve_all_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books


@app.get('/books/{id}',response_model=BookWithId)
def retrieve_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise HTTPException(status_code=404,detail='item not found')
    return book


@app.post('/books/',response_model=BookWithId)
def add_book(book: BookBase, db: Session = Depends(get_db)):
    db_book = Book(title=book.title, author=book.author,
                   year=book.year, isbn=book.isbn)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.put('/books/{id}',response_model=BookWithId)
def update_book(id: int, book: BookBase, db: Session = Depends(get_db)):
    book_to_update = db.query(Book).filter(Book.id == id).first()
    if book_to_update is None:
        raise HTTPException(status_code=404,detail='item not found')
    
    book_to_update.title = book.title
    book_to_update.author = book.author
    book_to_update.year = book.year
    book_to_update.isbn = book.isbn
    db.commit()
    return book_to_update


@app.delete('/books/{id}', response_model=BookWithId)
def delete_book(id: int, db: Session = Depends(get_db)):
    book_to_delete = db.query(Book).filter(Book.id == id).first()
    if book_to_delete is None:
        raise HTTPException(status_code=404,detail='item not found')
    
    db.delete(book_to_delete)
    db.commit()
    return book_to_delete