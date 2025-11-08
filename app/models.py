from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class BookBase(SQLModel):
    title: str = Field(index=True)
    author: str = Field(index=True)
    year: int
    price: float
    in_stock: bool = True
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

class Book(BookBase, table=True):  # Represents a table
    id: Optional[int] = Field(default=None, primary_key=True)

    def update_timestamp(self):
        self.updated_at = datetime.utcnow()
