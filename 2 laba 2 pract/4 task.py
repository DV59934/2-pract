class Counter:
    def __init__(self, count = 0):
        self.count = count

    def __add__(self):
        self.count += 1

    def reduction(self):
        self.count -= 1

score1 = Counter()
score2 = Counter(5)
print(f"Первый счётчик: {score1.count} \nВторой счётчик: {score2.count}")
score2.__add__()
print(f"Результат первого метода: {score2.count}")
score1.reduction()
print(f"Результат второго метода: {score1.count}")
