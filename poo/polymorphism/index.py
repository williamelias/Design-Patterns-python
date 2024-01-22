import random


class Animal:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.gender = gender
        self.age = age

    def make_sound(self):
        randon_sounds = ["cry cry", "beee", "ihon ihon"]

        return randon_sounds[random.randint(0, len(randon_sounds) - 1)]


class Cat(Animal):
    def make_sound(self):
        return "Meau"


class Dog(Animal):
    def make_sound(self):
        return "AuAu"
