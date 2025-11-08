from sqlmodel import Session, select
from typing import List, Optional
from .models import Book
from .schemas import BookCreate, BookUpdate, BookSearchResults


def create_book(session: Session, book: BookCreate) -> Book:
    db_book = Book.from_orm(book)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

def get_book(session: Session, book_id: int) -> Optional[Book]:
    return session.get(Book,book_id)


def get_books(session: Session, offset: int=0, limit: int=10) -> List[Book]:
    return session.exec(select(Book).offset(offset).limit(limit)).all()

def update_book(session: Session, book_id: int, book_data: BookUpdate) -> Optional[Book]:
    db_book = session.get(Book, book_id)
    if not db_book:
         return None
     
    for key, value in book_data.dict(exclude_unset=True).items():
         setattr(db_book, key, value)
    db_book.update_timestamp()
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


def delete_book(session: Session, book_id: int) -> bool:
    db_book = session.get(Book, book_id)
    if not db_book:
        return False
    session.delete(db_book)
    session.commit()
    return True