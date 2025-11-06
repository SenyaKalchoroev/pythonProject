from __future__ import annotations

from list_store import ListStore
from core import Movie


class MovieCollection(ListStore[Movie]):
    item_type_name = "movie"

    def add_movie(self, title: str, year: int | None = None) -> None:
        self.add(Movie(title, year))
