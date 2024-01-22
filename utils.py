import abc
import datetime


class Grade:
    def __init__(
        self, start_hour: datetime.datetime, end_hour: datetime.datetime
    ) -> None:
        self.start_hour = start_hour
        self.end_hour = end_hour

    def __str__(self) -> str:
        return f"{self.start_hour} - {self.end_hour}"


class CourseI(abc.ABC):
    @abc.abstractproperty
    def get_name(self) -> str:
        raise NotImplementedError

    @abc.abstractproperty
    def get_period(self) -> str:
        raise NotImplementedError


class Math(CourseI):
    def get_name(self) -> str:
        return "mathmatics"

    def get_period(self) -> str:
        return "second period"


class English(CourseI):
    def get_name(self) -> str:
        raise "english"

    def get_period(self) -> str:
        raise "third period"


class ClassRoom:
    def __init__(self, grade: Grade) -> None:
        self.grade = grade


class Student:
    pass


class Teacher:
    pass
