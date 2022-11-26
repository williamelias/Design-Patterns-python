import abc

"""
Requirement 1 
"""

# _____-> Good Way <-________


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make_sound(cls):
        raise NotImplementedError


class CatA(Animal):
    def make_sound(cls):
        return 'meau'


# before
class FoodA:
    def feed(self, cat: CatA):
        return 'feeding cat'


# after (good)
class FoodAnimal(FoodA):
    def feed(self, animal: Animal):
        return 'feeding animal'


# _____-> Bad Way <-________


class CatB(Animal):
    def make_sound(cls):
        return 'meau'


class BengalCat(CatB):
    def make_sound(cls):
        return 'meau bengal'


# before
class FoodB:
    def feed(self, cat: CatB):
        return 'feeding cat'


# after (bad)
class FoodBengalCat(FoodB):
    def feed(self, animal: BengalCat):
        return 'feeding animal'


# Requirement 1

