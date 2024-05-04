from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,index=True, unique=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    isbn = Column(String, index=True)