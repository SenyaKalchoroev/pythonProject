from __future__ import annotations

from typing import List

from list_store import ListStore
from core import Student


class StudentGroup(ListStore[Student]):
    item_type_name = "student"

    def add_student(self, name: str) -> None:
        self.add(Student(name))

    def list_students(self) -> List[Student]:
        return self.all()
