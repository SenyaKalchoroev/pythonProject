from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True)
class Book:
    title: str
    author: str


@dataclass(slots=True)
class Product:
    name: str
    qty: int = 1


@dataclass(slots=True)
class Student:
    name: str


@dataclass(slots=True)
class Song:
    title: str
    artist: str


@dataclass(slots=True)
class Task:
    text: str
    done: bool = False


@dataclass(slots=True)
class Movie:
    title: str
    year: int | None = None


@dataclass(slots=True)
class Event:
    title: str
    date: str
