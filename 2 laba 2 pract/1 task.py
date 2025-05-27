class Student:
    def __init__(self, surname, date_birth, number, progress): #конструктор, начальные атрибуты класса
        self.surname = surname
        self.date_birth = date_birth
        self.number = number
        self.progress = progress

    def __str__(self):
        return f"Фамилия: {self.surname}\n" \
               f"Дата рождения: {self.date_birth}\n" \
               f"Номер группы: {self.number}\n" \
               f"Успеваемость: {self.progress}"


def find_student(students, surname, date_of_birth):
    for student in students:
        if student.surname == surname and student.date_birth == date_of_birth:
            return student
    return None


students = [
    Student("Сабеля", "2005-12-12", "372", [4, 4, 3, 5, 4]),
    Student("Петров", "2008-04-26", "642", [4, 4, 5, 4, 5]),
    Student("Копытина", "2007-08-09", "202", [4, 4, 3, 4, 3]),
]

surname_input = input("Введите фамилию студента: ")
date_birth_input = input("Введите дату рождения студента (гггг-мм-дд): ")

student = find_student(students, surname_input, date_birth_input)

if student:
    print(student)

    n = input("Хотите изменить фамилию, дату рождения и группу? (y/n): ")
    if n.lower() == 'y':
        student.__surname = input("Введите новую фамилию: ")
        student.__date_birth = input("Введите новую дату рождения: ")
        student.__number = input("Введите новый номер группы: ")

        print("Информация о студенте обновлена:")
        print(student)
else:
    print("Студент не найден.")
