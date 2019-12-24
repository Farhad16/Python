class Duck:
    def quack(self):
        print("quack quack")


class MotherDuck(Duck):
    def quack(self):
        print("quack,my baby where are you")


class BabyDuck(Duck):
    def quack(self):
        print("Mom I'm here")


def quack(duckquack):
    duckquack.quack()


mother = MotherDuck()
quack(mother)
child = BabyDuck()
quack(child)
