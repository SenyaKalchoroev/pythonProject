from __future__ import annotations
from typing import Dict, Generic, List, Tuple, TypeVar
from base_store import KeyedMultiStore

K = TypeVar("K")
V = TypeVar("V")


class DictListStore(KeyedMultiStore[K, V], Generic[K, V]):
    pair_name: str = "mapping"

    def __init__(self) -> None:
        self._data: Dict[K, List[V]] = {}

    def add(self, key: K, value: V) -> None:
        self._data.setdefault(key, []).append(value)

    def get(self, key: K) -> List[V]:
        return list(self._data.get(key, []))

    def keys(self) -> List[K]:
        return list(self._data.keys())

    def items(self) -> List[Tuple[K, List[V]]]:
        return [(k, list(vs)) for k, vs in self._data.items()]

    def counts(self) -> Dict[K, int]:
        return {k: len(vs) for k, vs in self._data.items()}

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._data!r})"
