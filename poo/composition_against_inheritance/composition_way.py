import abc


class Engine(classmeta=abc.ABCMeta):
    @abc.abstractmethod
    def move(self):
        raise NotImplementedError


class Driver(classmeta=abc.ABCMeta):
    @abc.abstractmethod
    def navigate(self):
        raise NotImplementedError


class Robot(Driver):
    def navigate(self):
        return 'navigate'


class Human(Driver):
    def navigate(self):
        return 'navigate'


class CombustionEngine(Engine):
    def move(self):
        return 'move'


class EletricEngine(Engine):
    def move(self):
        return 'move'


class Transport:
    def __init__(self, engine: Engine, driver: Driver) -> None:
        self.__engine = engine()
        self.__driver = driver()
