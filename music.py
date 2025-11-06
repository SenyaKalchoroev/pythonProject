from __future__ import annotations

from typing import List

from list_store import ListStore
from core import Song


class Playlist(ListStore[Song]):
    item_type_name = "song"

    def add_song(self, title: str, artist: str) -> None:
        self.add(Song(title, artist))

    def all_songs(self) -> List[Song]:
        return self.all()
