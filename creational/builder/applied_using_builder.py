import abc

# Products


class Engine(metaclass=abc.ABCMeta):
    pass


class SportEngine(Engine):
    pass


class SUVEngine(Engine):
    pass


class Product(metaclass=abc.ABCMeta):
    pass


class Car(Product):
    def __init__(self) -> None:
        self.gps = None
        self.engine = None
        self.seats = None
        self.trip_computer = None


class Manual(Product):
    def __init__(self) -> None:
        self.gps = None
        self.engine = None
        self.seats = None
        self.trip_computer = None


# Builders


class Builder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_GPS(self):
        raise NotImplementedError

    @abc.abstractmethod
    def set_seats(self):
        raise NotImplementedError

    @abc.abstractmethod
    def set_engine(self):
        raise NotImplementedError

    @abc.abstractmethod
    def set_trip_computer(self):
        raise NotImplementedError

    @abc.abstractmethod
    def reset(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_result(self) -> Product:
        raise NotImplementedError


class CarBuilder(Builder):
    def __init__(self) -> None:
        self.__car = None
        self.reset()

    def set_GPS(self, gps: bool):
        self.__car.gps = gps

    def set_seats(self, seats: int):
        self.__car.seats = seats

    def set_engine(self, engine: Engine):
        self.__car.engine = engine

    def set_trip_computer(self, trip_computer: bool):
        self.__car.trip_computer = trip_computer

    def reset(self):
        self.__car = Car()

    def get_result(self) -> Car:
        car = self.__car
        self.reset()
        return car


class ManualBuilder(Builder):
    def __init__(self) -> None:
        self.__manual = None
        self.reset()

    def set_GPS(self, gps: str):
        self.__manual.gps = gps

    def set_seats(self, seats: str):
        self.__manual.seats = seats

    def set_engine(self, engine: str):
        self.__manual.engine = engine

    def set_trip_computer(self, trip_computer: str):
        self.__manual.trip_computer = trip_computer

    def reset(self):
        self.__manual = Manual()

    def get_result(self) -> Manual:
        manual = self.__manual
        self.reset()
        return manual


# Management
class Director:
    def __init__(self, builder: Builder) -> None:
        self.builder = builder

    def make_suv(self):
        self.builder.reset()
        self.builder.set_seats(4)
        self.builder.set_engine(SUVEngine())
        self.builder.set_trip_computer(True)
        self.builder.set_GPS(True)

    def make_car_sports(self):
        self.builder.reset()
        self.builder.set_seats(1)
        self.builder.set_engine(SportEngine())
        self.builder.set_trip_computer(True)
        self.builder.set_GPS(False)


class Client:
    def __init__(self) -> None:
        self.product = None

    def car_maker(self):
        builder = CarBuilder()

        director = Director(builder=builder)

        director.make_car_sports()

        car = builder.get_result()

        self.product = car
