class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyFish(Flyer, Swimmer):
    pass


f = FlyFish()
f.fly()
