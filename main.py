from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine) # the creator 

# This function to take a ticket to the Database
def get_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Book(BaseModel):
    title:str
    author:str
    pages: int
    is_published: bool

    class Config():
        from_attributes = True

@app.post("/books")
def add_book(book:Book ,db: Session = Depends(get_connection)):
    db_book=models.DBBook(title = book.title,
                             author = book.author,
                             pages = book.pages,
                              is_published = book.is_published )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books")
def get_all_books(db: Session = Depends(get_connection)):
    db_all_books = db.query(models.DBBook).all()
    return db_all_books
@app.get("/books/{id}")
def get_books(id:int, db: Session = Depends(get_connection)):
    db_book = db.query(models.DBBook).filter(models.DBBook.id == id).first()

    if not db_book:
        raise HTTPException(status_code=404, detail="Book Not Found")
    else:
        return db_book

@app.put("/books/{id}")
def updateBook(id:int, book:Book, db: Session = Depends(get_connection)):
    element = db.query(models.DBBook).filter(models.DBBook.id == id).first()
    if not element:
        raise HTTPException(status_code=404, detail="Book is not found")
    else:
       element.title = book.title
       element.pages = book.pages
       element.is_published = book.is_published
       element.author = book.author

       db.commit()
       db.refresh(element)
       return element
@app.delete("/books/{id}")
def delete_book(id:int, db: Session = Depends(get_connection)):
    element = db.query(models.DBBook).filter(models.DBBook.id == id).first()

    if not element:
        raise HTTPException(status_code=404, detail="Book Not Found")
    else:
        db.delete(element)
        db.commit()
        return {"Message": "Deleted"}
