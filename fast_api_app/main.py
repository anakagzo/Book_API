from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI()

list_of_books = [{'title': 'things fall apart','author': 'chinua achebe', 'year': 1998, 'isbn': '2345'},
                 {'title': 'no longer at ease','author': 'chinua achebe', 'year': 1998, 'isbn': '2387627'},
                 {'title': 'dark knights','author': 'josh publicius', 'year': 2001, 'isbn': '2000'},]

books = []

def get_id():
    return len(books)+1


class Book(BaseModel):
    id: int = Field(default_factory= lambda: get_id())
    title: str
    author: str
    year: int
    isbn: str

    

for item in list_of_books:
    book = Book(
        
        title=item['title'],
        author=item['author'],
        year=item['year'],
        isbn=item['isbn']
    ) 

    books.append(book)


@app.get('/books', response_model=list[Book])
def book_list():
    return books


@app.get('/books/{id}', response_model=Book)
def retrieve_book(id: int):
    if id not in range(1,len(books)+1):
        raise HTTPException(status_code=404, detail='item not found')
    book = books[id-1]
    return book


@app.post('/books')
def add_book(book: Book):
    book.id = len(books)+1
    books.append(book)
    return books


@app.put('/books/{id}')
def update_book(id: int, book: Book):
    if id not in range(1,len(books)+1):
        raise HTTPException(status_code=404, detail='item not found')
    book.id = id
    books[id-1] = book
    return books


@app.delete('/books/{id}')
def delete_book(id: int):
    if id not in range(1,len(books)+1):
        raise HTTPException(status_code=404, detail='item not found')
    books.pop(id-1)
    return books