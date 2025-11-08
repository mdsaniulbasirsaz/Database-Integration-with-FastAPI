from typing import Optional, List
from sqlmodel import SQLModel
from datetime import datetime


class BookCreate(SQLModel):
    title: str
    author: str
    year: int
    price: float
    in_stock: bool=True
    description: Optional[str]=None 


class BookRead(SQLModel):
    id: int
    title: str
    author: str
    year: int
    price: float
    in_stock: bool
    description: Optional[str]
    created_at: datetime
    updated_at: datetime


class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    price: Optional[float] = None
    in_stock: Optional[float] = None
    description: Optional[str] = None

class BookSearchResults(SQLModel):
    results: List[BookRead]
    total: int
    page: int
    size: int