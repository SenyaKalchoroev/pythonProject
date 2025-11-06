from __future__ import annotations

from list_store import ListStore
from core import Event


class EventSchedule(ListStore[Event]):
    item_type_name = "event"

    def add_event(self, title: str, date: str) -> None:
        self.add(Event(title, date))
