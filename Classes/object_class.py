# every class in python directly or indirectly inherit object class


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(isinstance(m, object))
print(issubclass(Mammal, object))
