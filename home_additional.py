import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

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

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Zoo saved to {filename}.")

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        print(f"Zoo loaded from {filename}.")
        return zoo

zoo = Zoo()

zoo.add_animal(Bird("Tweety", 3))
zoo.add_animal(Mammal("Hunty", 2))
zoo.add_animal(Reptile("Wirey", 1))

zoo.add_employee(ZooKeeper("Nina"))
zoo.add_employee(Veterinarian("Kirill"))

zoo.save_to_file('zoo.pkl')

loaded_zoo = Zoo.load_from_file('zoo.pkl')

loaded_zoo.make_all_sounds()

loaded_zoo.show_employees()

loaded_zoo.feed_all_animals()

loaded_zoo.heal_all_animals()
