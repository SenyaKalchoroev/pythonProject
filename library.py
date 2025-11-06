from __future__ import annotations

from typing import List

from list_store import ListStore
from models import Book


class Library(ListStore[Book]):
    item_type_name = "book"

    def add_book(self, title: str, author: str) -> None:
        self.add(Book(title, author))

    def list_books(self) -> List[Book]:
        return self.all()
