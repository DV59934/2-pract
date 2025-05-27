class Numbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def display(self):
        print(f"Число 1: {self.num1}")
        print(f"Число 2: {self.num2}")

    def change_numbers(self, new_num1, new_num2):
        self.num1 = new_num1
        self.num2 = new_num2

    def summ(self):
        return self.num1 + self.num2

    def maxi(self):
        return max(self.num1, self.num2)

numbers = Numbers(5, 3)
print("Исходные числа:")
numbers.display()
print(f"\nСумма: {numbers.summ()}")
print(f"\nНаибольшее число: {numbers.maxi()}")

print("\nИзменяем числа на 4 и 7:")
numbers.change_numbers(4, 7)
numbers.display()

print(f"\nНовая сумма: {numbers.summ()}")
print(f"\nНовое наибольшее число: {numbers.maxi()}")
