from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Dict, Tuple

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class Store(ABC, Generic[T]):
    @abstractmethod
    def add(self, item: T) -> None: ...
    @abstractmethod
    def all(self) -> List[T]: ...
    @abstractmethod
    def count(self) -> int: ...
    @abstractmethod
    def clear(self) -> None: ...


class KeyedMultiStore(ABC, Generic[K, V]):
    @abstractmethod
    def add(self, key: K, value: V) -> None: ...
    @abstractmethod
    def get(self, key: K) -> List[V]: ...
    @abstractmethod
    def keys(self) -> List[K]: ...
    @abstractmethod
    def items(self) -> List[Tuple[K, List[V]]]: ...
    @abstractmethod
    def counts(self) -> Dict[K, int]: ...
