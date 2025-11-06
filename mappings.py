from __future__ import annotations
from typing import List, Tuple

from dict_list_store import DictListStore


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


class StudentGrades(DictListStore[str, tuple[str, float]]):
    def add_grade(self, student: str, subject: str, grade: float) -> None:
        self.add(student, (subject, grade))

    def grades_of(self, student: str) -> list[tuple[str, float]]:
        return self.get(student)
