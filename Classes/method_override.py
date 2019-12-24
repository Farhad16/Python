class Animal:

    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):

    def __init__(self):
        print("Mammal constructor")
        self.weight = 5
        super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(m.weight)
print(m.age)
