from __future__ import annotations

from library import Library
from shopping import ShoppingCart
from students import StudentGroup
from mappings import EmployeeProjects, StudentGrades

def run_demo() -> None:
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

if __name__ == "__main__":
    run_demo()
