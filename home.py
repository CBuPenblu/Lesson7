#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется
# (например, различный звук для `make_sound()`).
#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says: Pkaw!")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} says: Hong-Kong!")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} says: Shhhhhhh!")

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        print(f"{self.name} is working as a {self.position}.")

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the zoo.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to the zoo staff.")

    def make_all_sounds(self):
        for animal in self.animals:
            animal.make_sound()

    def show_employees(self):
        for employee in self.employees:
            employee.work()

    def feed_all_animals(self):
        for employee in self.employees:
            if isinstance(employee, ZooKeeper):
                for animal in self.animals:
                    employee.feed_animal(animal)

    def heal_all_animals(self):
        for employee in self.employees:
            if isinstance(employee, Veterinarian):
                for animal in self.animals:
                    employee.heal_animal(animal)

zoo = Zoo()

zoo.add_animal(Bird("Tweety", 3))
zoo.add_animal(Mammal("Hunty", 2))
zoo.add_animal(Reptile("Wirey", 2))

zoo.add_employee(ZooKeeper("Nina"))
zoo.add_employee(Veterinarian("Kirill"))

zoo.make_all_sounds()

zoo.show_employees()

zoo.feed_all_animals()

zoo.heal_all_animals()
