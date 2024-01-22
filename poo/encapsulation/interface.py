import abc


class FlyingTransportI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly(origin: str, destination: str, passangers: int):
        raise NotImplementedError


class Helicopter(FlyingTransportI):
    def fly(self, origin: str, destination: str, passangers: int) -> str:
        return f"Flying on helicopter - origin/destination/passangers: {origin}/{destination}/{passangers}"


class Airplain(FlyingTransportI):
    def fly(self, origin: str, destination: str, passangers: int) -> str:
        return f"Flying on airplain - origin/destination/passangers: {origin}/{destination}/{passangers}"


class DomesticatedGryphon(FlyingTransportI):
    def fly(self, origin: str, destination: str, passangers: int) -> str:
        return f"Flying on DomesticatedGryphon - origin/destination/passangers: {origin}/{destination}/{passangers}"


class Airport:
    def __init__(self, origin, destination, passangers) -> None:
        self.__origin = origin
        self.__destination = destination
        self.__passangers = passangers

    def accept(self, vehicle: FlyingTransportI):
        return vehicle.fly(self.__origin, self.__destination, self.__passangers)


# Usages

"""
airport = Airport('damasco','são paulo',100)

airport.accept(DomesticatedGryphon())
output: 'Flying on DomesticatedGryphon - origin/destination/passangers: damasco/são paulo/100'

airport.accept(Helicopter())
output: 'Flying on helicopter - origin/destination/passangers: damasco/são paulo/100'

"""
