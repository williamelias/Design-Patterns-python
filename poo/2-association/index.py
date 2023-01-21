import abc

class CourseI(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def items(cls):
        raise NotImplementedError


class Math(CourseI):
    @property
    def items(self):
        return ['Logic','calculation']

class Person:
    def __init__(self,name:str,gender:str,age:int) -> None:
        self.name = name 
        self.gender = gender 
        self.age = age

class Teacher(Person):
    def __init__(self,name:str,gender:str,age:int) -> None:
        super().__init__(name,gender,age)

class Student(Person):
    def __init__(self,name:str,gender:str,age:int) -> None:
        super().__init__(name,gender,age)


class PrivateClass:
    def __init__(self,student:Student,teacher:Teacher) -> None:
        self.__student = student
        self.__teacher = teacher
    
    def studying_now(self,course:CourseI):
        course_items = course.items

        return f"Teacher {self.__teacher.name} and student {self.__student.name} are studying {course_items} now."