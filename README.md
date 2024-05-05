The Book API is an API created to manage a book database. 
it is built using FastAPI and SQLAlchemy. 
it provides endpoints to perform basic CRUD (Create, Read, Update, Delete) operations on books.

**Endpoints**

**GET /books**
  Retrieves a list of all books in the database
  
**GET /books/{id}** 
  Retrieves information about a specific book
  base on the _id_
  
**POST /books**
  Adds a new book to the database.
  
**PUT /books/{id}**
  Updates the information of a book
  identified by _id_ 
  
**DELETE /books/{id}**
  Deletes a book from the database 
  identified by _id_


**How to Setup the Application**

1. clone the repository:
   
   _command_: git clone https://github.com/anakagzo/Book_API.git
   
2. install dependencies:
   
   dependencies: fastapi, sqlalchemy

3. run the application:
   
   _command_: cd into the directory that contains main.py file,
              type uvicorn main:app --reload

**How the API works**

1. To retrieve all books:
   
   endpoint: GET /books

2. To retrieve a particular book:
   
   endpoint: GET /books/{book_id}

3. To Add a new book:
   
   endpoint: POST /books
   
   required params:
   
   {
   
     'title': _string_,
   
     'author': _string_,
   
     'year': _integer_,
   
     'isbn': _string_
   
   }
   
4. To Update the information of a new book:
   
   endpoint: PUT /books/{book_id}
   
   required params:
   
   {
   
     'title': _string_,
   
     'author': _string_,
   
     'year': _integer_,
   
     'isbn': _string_
   
   }

5. To Delete a book
    
   endpoint: DELETE /books/{book_id}    

**Documentation**

the application contains a Swagger documentation 
that can be used to test the API endpoints. 

the Swagger documentation can be accessed at
'http://localhost:8000/docs' after 
cloning the project and running the application 
on the local server.

