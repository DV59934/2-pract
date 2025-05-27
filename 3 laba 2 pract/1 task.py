class Worker:
    def __init__(self, name, surname, rate, days):
        self.surname = surname
        self.days = days
        self.name = name
        self.rate = rate
    def GetSalary(self):
        print("Зарплата работника составляет:", self.rate * self.days, "рублей")

worker1 = Worker("Nana", "Kerner", 600, 19)
worker1.GetSalary()
