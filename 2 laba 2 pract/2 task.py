class Train:
    def __init__(self, destination, number, departure_time):
        self.destination = destination
        self.departure_time = departure_time
        self.number = number

    def __str__(self):
        return f"Пункт назначения: {self.destination}\n" \
               f"Номер поезда: {self.number}\n" \
               f"Время отправления: {self.departure_time}"


trains = [
    Train("Москва", "733926", "17:24"),
    Train("Краснодар", "593299", "03:45"),
    Train("Павлодар", "39824", "12:05"),
]

number = input("Введите номер поезда: ")

found_train = None
for train in trains:
    if train.number == number:
        found_train = train
        break

if found_train:
    print(found_train)
else:
    print("Поезд не найден")
