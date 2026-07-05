from sqlalchemy import Column, Integer, Float, String, Boolean
from database import Base

class DBBook(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String, index=True)
    pages = Column(Integer)
    is_published=Column(Boolean)



