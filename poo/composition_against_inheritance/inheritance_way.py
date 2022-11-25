# Inheritance Way


class Transport:
    pass


class Truck(Transport):
    pass


class Car(Transport):
    pass


class EletricTruck(Truck):
    pass


class EletricCar(Car):
    pass


class CombustionEngineTruck(Truck):
    pass


class CombustionEngineCar(Car):
    pass


class AutopilotEletricTruck(EletricTruck):
    pass


class AutopilotEletricCar(EletricCar):
    pass


class AutopilotCombustionEngineTruck(CombustionEngineTruck):
    pass


class AutopilotCombustionEngineCar(CombustionEngineCar):
    pass
