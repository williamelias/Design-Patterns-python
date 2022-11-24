import typing as tp
import abc

ITEMS = {
    'math': ['Logic','Calc'],
    'history': ['French Revolution','First world War']
}

# Strong Dependence
class CourseConcrete:
    def __init__(self,items:tp.Iterable[str]) -> None:
        self.__items = items
    
    @property
    def items(self):
        return f'Items of course {self.__items}'

class TeacherStrong:
    def list_items(self,course:CourseConcrete):
        return course.items

# Weak Dependence

class CourseI(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def items(cls):
        raise NotImplementedError


class Math(CourseI):
    def __init__(self,items:tp.Iterable[str]=[]) -> None:
        self.__items = items or ITEMS['math']

    @property
    def items(self):
        return f'Items of course {self.__items}'

class History(CourseI):
    def __init__(self,items:tp.Iterable[str]=[]) -> None:
        self.__items = items or ITEMS['history']
    
    @property
    def items(self):
        return f'Items of course {self.__items}'


class TeacherWeak:
    def list_items(self,course:CourseI):
        return course.items