import abc

"""
Requirement 1 - method parameter type
"""

# _____-> Good Way <-________


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make_sound(cls) -> str:
        raise NotImplementedError


class CatA(Animal):
    def make_sound(cls) -> str:
        return 'meau'


# before
class FoodA:
    def feed(self, cat: CatA)->:
        return 'feeding cat'


# after (good)
class FoodAnimal(FoodA):
    def feed(self, animal: Animal)->:
        return 'feeding animal'


# _____-> Bad Way <-________


class CatB(Animal):
    def make_sound(cls)->str:
        return 'meau'


class BengalCat(CatB):
    def make_sound(cls)->str:
        return 'meau bengal'


# before
class FoodB:
    def feed(self, cat: CatB)->str:
        return 'feeding cat'


# after (bad)
class FoodBengalCat(FoodB):
    def feed(self, animal: BengalCat)->str:
        return 'feeding animal'


# Requirement 2 - method return type

# _____-> Good Way <-________

class CustomAnimal(Animal):
    def make_sound(self)->str:
        return 'aaaa'

# _____-> Bad Way <-________

class CustomAnimalB(Animal):
    def make_sound(self)->int:
        return 1