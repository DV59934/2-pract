class Worker:
    def __init__(self, name, surname, rate, days):
        self.surname = surname
        self.days = days
        self.name = name
        self.rate = rate
    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_rate(self):
        return self.rate
    def get_days(self):
        return self.days
    def GetSalary(self):
        print("Зарплата работника составляет:", self.rate * self.days, "рублей")

worker1 = Worker("Nana", "Kerner", 600, 19)
worker1.GetSalary()
print(f"{worker1.get_name()} \n"
      f"{worker1.get_surname()} \n"
      f"{worker1.get_rate()} \n"
      f"{worker1.get_days()}")
