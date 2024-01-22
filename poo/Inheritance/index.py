import abc


# Interfaces
class WildI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def prey(name: str):
        raise NotImplementedError


class DomesticdI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def portion(name: str):
        raise NotImplementedError


# Concret class
class Animal:
    def __init__(self, name, gender, age, sound) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.sound = sound


# Inheritance example
class DomesticCat(Animal, DomesticdI):
    def __init__(self, name, gender, age, sound) -> None:
        super().__init__(name, gender, age)

    def portion(self, name: str):
        return f"I eat {name}"


class WildCat(Animal, WildI):
    def __init__(self, name, gender, age, sound) -> None:
        super().__init__(name, gender, age)

    def prey(self, name: str):
        return f"I hunt {name}"
