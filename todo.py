from __future__ import annotations

from typing import List

from list_store import ListStore
from core import Task


class TodoList(ListStore[Task]):
    item_type_name = "task"

    def add_task(self, text: str) -> None:
        self.add(Task(text))

    def tasks(self) -> List[Task]:
        return self.all()
