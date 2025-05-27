import sqlite3

class Student:
    def __init__(self, name, surname, patronymic, group, grades):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group = group
        if len(grades) != 4:
            print("Успеваемость должна содержать 4 оценки")
        self.grades = grades

connect = sqlite3.connect("Student.db")
cursor = connect.cursor()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            patronymic TEXT,
            group_number TEXT,
            grades TEXT,
            average REAL
        )
    """)


def add_student(student):  # Добавление студента
    connect = sqlite3.connect('Students.db')
    cursor = connect.cursor()
    average = sum(student.grades) / len(student.grades)
    cursor.execute("""
        INSERT INTO students 
        (name, surname, patronymic, group_number, grades, average)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
        student.name,
        student.surname,
        student.patronymic,
        student.group,
        ','.join(map(str, student.grades)), #сохранение оценок как строка с разделителями
        average
    ))
    connect.commit()
    connect.close()

def all_students():  # Показ всех студентов
    connect = sqlite3.connect('Students.db')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM students")

    print(f"\nВсе студенты:")
    all_rows = cursor.fetchall()
    for row in all_rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}, Отчество: {row[3]}, "
              f"Группа: {row[4]}, Оценки: {row[5]}, Средний балл: {row[6]:.2f}")
    connect.close()

def input_student(return_as=False):
    print("Введите данные студента:")
    name = input("Имя: ")
    surname = input("Фамилия: ")
    patronymic = input("Отчество: ")
    group = input("Группа: ")

    while True:
        grades_input = input("Введите 4 оценки (через пробел): ").split()
        grades = [int(grade) for grade in grades_input]
        if len(grades) != 4:
            print("Успеваемость должна содержать 4 оценки")
            continue
        if not all(2 <= grade <= 5 for grade in grades):
            print("Оценки должны иметь диапозон от 2 до 5(включая)")
            continue
        break
    if return_as:
        return [name, surname, patronymic, group, grades]
    return Student(name, surname, patronymic, group, grades)

def edit_student():
    connect = sqlite3.connect('Students.db')
    cursor = connect.cursor()
    all_students()
    id_student = input("Выберите ID студента для редактирования: ")
    student_info = input_student(return_as=True)
    average = sum(student_info[4]) / len(student_info[4])

    cursor.execute("""
        UPDATE students SET
        name = ?,
        surname = ?,
        patronymic = ?,
        group_number = ?,
        grades = ?,
        average = ?
        WHERE id = ?
    """, (
        student_info[0],
        student_info[1],
        student_info[2],
        student_info[3],
        ','.join(map(str, student_info[4])),
        average,
        id_student
    ))
    if cursor.rowcount > 0:
        print("Данные студента обновлены!")
    else:
        print("Студент не найден.")
    connect.commit()
    connect.close()


def del_student():
    connect = sqlite3.connect('Students.db')
    cursor = connect.cursor()
    all_students()
    id_student = input("Выберите ID студента для удаления: ")
    cursor.execute("DELETE FROM students WHERE id = ?", (id_student,))
    if cursor.rowcount > 0:
        print("Студент удалён!")
    else:
        print("Студент не найден.")
    connect.commit()
    connect.close()



while True:
    print("\n1 - Добавить нового студента\n"
          "2 - Просмотр всех студентов\n"
          "3 - Просмотр одного студента\n"
          "4 - Редактирование студента\n"
          "5 - Удаление студента\n"
          "6 - Средний балл студентов группы\n"
          "7 - Завершить программу")
    action = input("Выберите действие: ")

    if action == "1":
        student = input_student()
        add_student(student)
        print("Студент успешно добавлен")

    elif action == "2":
        all_students()

    elif action == "3":
        connect = sqlite3.connect('Students.db')
        cursor = connect.cursor()
        id_student = input("Введите ID студента для вывода: ")
        cursor.execute("SELECT * FROM students WHERE id = ?", (id_student,))
        row = cursor.fetchone()
        if row:
            print(f"\nID: {row[0]}")
            print(f"Имя: {row[1]}")
            print(f"Фамилия: {row[2]}")
            print(f"Отчество: {row[3]}")
            print(f"Группа: {row[4]}")
            print(f"Оценки: {row[5]}")
            print(f"Средний балл: {row[6]:.2f}\n")
        else:
            print("Студент не найден")
            connect.close()

    elif action == "4":
        edit_student()

    elif action == "5":
        del_student()

    elif action == "6":
        connect = sqlite3.connect('Students.db')
        cursor = connect.cursor()
        group_number = input("Введите группу для вывода среднего балла: ")
        cursor.execute("SELECT average FROM students WHERE group_number = ?", (group_number,))
        rows = cursor.fetchall()
        if not rows:
            print("В этой группе нет студентов")
            connect.close()
            continue

        total = sum(row[0] for row in rows)
        average = total / len(rows)
        print(f"Средний балл группы {group_number}: {average:.2f}")
        connect.close()

    elif action == "7":
        break
    else:
        print("Неизвестное действие. Введите число от 1 до 7")
