from __future__ import annotations

from typing import Generic, Iterable, Callable, List, TypeVar

from base_store import Store

T = TypeVar("T")


class ListStore(Store[T], Generic[T]):
    item_type_name: str = "item"

    def __init__(self, items: Iterable[T] | None = None) -> None:
        self._items: List[T] = list(items) if items else []

    def add(self, item: T) -> None:
        self._items.append(item)

    def all(self) -> List[T]:
        return list(self._items)

    def count(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items.clear()

    def find(self, predicate: Callable[[T], bool]) -> List[T]:
        return [x for x in self._items if predicate(x)]

    @classmethod
    def from_iterable(cls, data: Iterable[T]) -> "ListStore[T]":
        return cls(items=data)

    @staticmethod
    def not_none(x: T | None) -> bool:
        return x is not None

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._items!r})"
