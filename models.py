from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class DBBook(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String, index=True)
    pages = Column(Integer)
    is_published=Column(Boolean)

    author_id=Column(Integer, ForeignKey("authors.id"))
    author = relationship("DBAuthor", back_populates="books")

class DBAuthor(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    bio= Column(String)

    books = relationship("DBBook", back_populates="author")
