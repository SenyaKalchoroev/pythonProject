from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, List, Dict, Callable, Iterable, Tuple

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")

class ListStore(Generic[T]):
    item_type_name: str = "item"

    def __init__(self, items: Iterable[T] | None = None) -> None:
        self._items: List[T] = list(items) if items else []

    def add(self, item: T) -> None:
        self._items.append(item)

    def all(self) -> List[T]:
        return list(self._items)

    def find(self, predicate: Callable[[T], bool]) -> List[T]:
        return [x for x in self._items if predicate(x)]

    def count(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items.clear()

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


class DictListStore(Generic[K, V]):
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


class Library(ListStore[Book]):
    item_type_name = "book"

    def add_book(self, title: str, author: str) -> None:
        self.add(Book(title, author))

    def list_books(self) -> List[Book]:
        return self.all()


class ShoppingCart(ListStore[Product]):
    item_type_name = "product"

    def add_product(self, name: str, qty: int = 1) -> None:
        self.add(Product(name, qty))

    def total_quantity(self) -> int:
        return sum(p.qty for p in self.all())


class StudentGroup(ListStore[Student]):
    item_type_name = "student"

    def add_student(self, name: str) -> None:
        self.add(Student(name))

    def list_students(self) -> List[Student]:
        return self.all()


class Playlist(ListStore[Song]):
    item_type_name = "song"

    def add_song(self, title: str, artist: str) -> None:
        self.add(Song(title, artist))

    def all_songs(self) -> List[Song]:
        return self.all()


class TodoList(ListStore[Task]):
    item_type_name = "task"

    def add_task(self, text: str) -> None:
        self.add(Task(text))

    def tasks(self) -> List[Task]:
        return self.all()


class MovieCollection(ListStore[Movie]):
    item_type_name = "movie"

    def add_movie(self, title: str, year: int | None = None) -> None:
        self.add(Movie(title, year))


class EventSchedule(ListStore[Event]):
    item_type_name = "event"

    def add_event(self, title: str, date: str) -> None:
        self.add(Event(title, date))


class SimpleNameList(ListStore[str]):
    label: str = "item"

    def add_name(self, name: str) -> None:
        self.add(name)

    def names(self) -> List[str]:
        return self.all()


class FriendList(SimpleNameList):
    label = "friend"


class CarGarage(SimpleNameList):
    label = "car"


class PhotoAlbum(SimpleNameList):
    label = "photo"


class Zoo(SimpleNameList):
    label = "animal"


class GameInventory(SimpleNameList):
    label = "item"


class Blog(SimpleNameList):
    label = "post"


class Classroom(SimpleNameList):
    label = "pupil"


class MusicBand(SimpleNameList):
    label = "member"


class ShoppingList(SimpleNameList):
    label = "product"


class LibraryShelf(SimpleNameList):
    label = "book"


class TicketSystem(SimpleNameList):
    label = "ticket"


class PetOwner(SimpleNameList):
    label = "pet"


class StudyPlan(SimpleNameList):
    label = "topic"


class Workshop(SimpleNameList):
    label = "tool"


class CityTour(SimpleNameList):
    label = "place"


class MoviePlaylist(SimpleNameList):
    label = "movie"


class Conference(SimpleNameList):
    label = "participant"


class DailyJournal(SimpleNameList):
    label = "entry"


class WorkshopSchedule(SimpleNameList):
    label = "task"


class ProductCatalog(SimpleNameList):
    label = "product"


class TravelDestinations(SimpleNameList):
    label = "country"


class Bank(SimpleNameList):
    label = "account"


class EmployeeProjects(DictListStore[str, str]):
    pair_name = "employee->projects"

    def add_project(self, employee: str, project: str) -> None:
        self.add(employee, project)

    def projects_of(self, employee: str) -> List[str]:
        return self.get(employee)


class StudentCourses(DictListStore[str, str]):
    pair_name = "student->courses"

    def register(self, student: str, course: str) -> None:
        self.add(student, course)

    def courses_of(self, student: str) -> List[str]:
        return self.get(student)


class LibraryUsers(DictListStore[str, str]):
    pair_name = "reader->books"

    def give_book(self, reader: str, book_title: str) -> None:
        self.add(reader, book_title)

    def books_of(self, reader: str) -> List[str]:
        return self.get(reader)


class TeacherSubjects(DictListStore[str, str]):
    def assign(self, teacher: str, subject: str) -> None:
        self.add(teacher, subject)

    def subjects_of(self, teacher: str) -> List[str]:
        return self.get(teacher)


class ProjectTeams(DictListStore[str, str]):
    def add_member(self, project: str, employee: str) -> None:
        self.add(project, employee)

    def members_of(self, project: str) -> List[str]:
        return self.get(project)


class CourseAssignments(DictListStore[str, str]):
    def add_assignment(self, course: str, task: str) -> None:
        self.add(course, task)

    def assignments_of(self, course: str) -> List[str]:
        return self.get(course)


class WorkshopParticipants(DictListStore[str, str]):
    def enroll(self, workshop: str, person: str) -> None:
        self.add(workshop, person)

    def participants_of(self, workshop: str) -> List[str]:
        return self.get(workshop)


class TeamTasks(DictListStore[str, str]):
    def assign_task(self, team: str, task: str) -> None:
        self.add(team, task)

    def tasks_of(self, team: str) -> List[str]:
        return self.get(team)


class StudentGrades(DictListStore[str, Tuple[str, float]]):
    def add_grade(self, student: str, subject: str, grade: float) -> None:
        self.add(student, (subject, grade))

    def grades_of(self, student: str) -> List[Tuple[str, float]]:
        return self.get(student)


class EventAttendees(DictListStore[str, str]):
    def add_attendee(self, event: str, person: str) -> None:
        self.add(event, person)

    def attendees_of(self, event: str) -> List[str]:
        return self.get(event)


class BookGenres(DictListStore[str, str]):
    def add_book(self, genre: str, title: str) -> None:
        self.add(genre, title)

    def books_of(self, genre: str) -> List[str]:
        return self.get(genre)


class CourseMaterials(DictListStore[str, str]):
    def add_material(self, course: str, material: str) -> None:
        self.add(course, material)

    def materials_of(self, course: str) -> List[str]:
        return self.get(course)


class ConferenceSpeakers(DictListStore[str, str]):
    def add_speaker(self, conf: str, speaker: str) -> None:
        self.add(conf, speaker)

    def speakers_of(self, conf: str) -> List[str]:
        return self.get(conf)


class StudentClubs(DictListStore[str, str]):
    def join(self, club: str, student: str) -> None:
        self.add(club, student)

    def members_of(self, club: str) -> List[str]:
        return self.get(club)


class ProjectDeadlines(DictListStore[str, str]):
    def add_deadline(self, project: str, deadline: str) -> None:
        self.add(project, deadline)

    def deadlines_of(self, project: str) -> List[str]:
        return self.get(project)


class CourseStudents(DictListStore[str, str]):
    def add_student(self, course: str, student: str) -> None:
        self.add(course, student)

    def students_of(self, course: str) -> List[str]:
        return self.get(course)


class EmployeeTrainings(DictListStore[str, str]):
    def add_training(self, employee: str, training: str) -> None:
        self.add(employee, training)

    def trainings_of(self, employee: str) -> List[str]:
        return self.get(employee)


class CityEvents(DictListStore[str, str]):
    def add_event(self, city: str, event: str) -> None:
        self.add(city, event)

    def events_of(self, city: str) -> List[str]:
        return self.get(city)


class LibrarySections(DictListStore[str, str]):
    def add_book(self, section: str, title: str) -> None:
        self.add(section, title)

    def books_of(self, section: str) -> List[str]:
        return self.get(section)


class TeacherStudents(DictListStore[str, str]):
    def add_student(self, teacher: str, student: str) -> None:
        self.add(teacher, student)

    def students_of(self, teacher: str) -> List[str]:
        return self.get(teacher)


class PlayerTeams(DictListStore[str, str]):
    def add_team(self, player: str, team: str) -> None:
        self.add(player, team)

    def teams_of(self, player: str) -> List[str]:
        return self.get(player)


class StudentAssignments(DictListStore[str, str]):
    def add_assignment(self, student: str, assignment: str) -> None:
        self.add(student, assignment)

    def assignments_of(self, student: str) -> List[str]:
        return self.get(student)


class MusicAlbums(DictListStore[str, str]):
    def add_album(self, artist: str, album: str) -> None:
        self.add(artist, album)

    def albums_of(self, artist: str) -> List[str]:
        return self.get(artist)


class TravelGroups(DictListStore[str, str]):
    def add_member(self, group: str, person: str) -> None:
        self.add(group, person)

    def members_of(self, group: str) -> List[str]:
        return self.get(group)


class WorkshopTopics(DictListStore[str, str]):
    def add_topic(self, workshop: str, topic: str) -> None:
        self.add(workshop, topic)

    def topics_of(self, workshop: str) -> List[str]:
        return self.get(workshop)


class EmployeeSkills(DictListStore[str, str]):
    def add_skill(self, employee: str, skill: str) -> None:
        self.add(employee, skill)

    def skills_of(self, employee: str) -> List[str]:
        return self.get(employee)


class DepartmentEmployees(DictListStore[str, str]):
    def add_employee(self, department: str, employee: str) -> None:
        self.add(department, employee)

    def employees_of(self, department: str) -> List[str]:
        return self.get(department)


class CourseTopics(DictListStore[str, str]):
    def add_topic(self, course: str, topic: str) -> None:
        self.add(course, topic)

    def topics_of(self, course: str) -> List[str]:
        return self.get(course)


class LibraryBorrowings(DictListStore[str, str]):
    def add_book(self, reader: str, title: str) -> None:
        self.add(reader, title)

    def books_of(self, reader: str) -> List[str]:
        return self.get(reader)


class EmployeeTasks(DictListStore[str, str]):
    def add_task(self, employee: str, task: str) -> None:
        self.add(employee, task)

    def tasks_of(self, employee: str) -> List[str]:
        return self.get(employee)


if __name__ == "__main__":
    lib = Library()
    lib.add_book("Гарри Поттер", "Дж. Роулинг")
    lib.add_book("Война и мир", "Л. Толстой")
    print("Книги:", lib.list_books())

    cart = ShoppingCart()
    cart.add_product("Яблоко", 3)
    cart.add_product("Хлеб", 1)
    print("Количество товаров:", cart.total_quantity())

    group = StudentGroup()
    for name in ["Алиса", "Боб", "Чарли"]:
        group.add_student(name)
    print("Студенты:", [s.name for s in group.list_students()])

    emp_proj = EmployeeProjects()
    emp_proj.add_project("Иванов", "CRM")
    emp_proj.add_project("Иванов", "Мобильное приложение")
    emp_proj.add_project("Петров", "Сайт")
    print("Проекты Иванова:", emp_proj.projects_of("Иванов"))

    grades = StudentGrades()
    grades.add_grade("Мария", "Математика", 4.5)
    grades.add_grade("Мария", "Физика", 5.0)
    print("Оценки Марии:", grades.grades_of("Мария"))
