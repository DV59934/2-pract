class designer:
    def __init__(self, parameter1 = "default1", parameter2 = "default2"):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        print(f"Объекты: {parameter1}, {parameter2}")
    def __del__(self):
        print(f"Удаление объектов: {self.parameter1}, {self.parameter2}")

object_1 = designer()
object_2 = designer("463", "library")
object_3 = designer("text", "elements")
print()
del object_1, object_2, object_3
