import abc


class TransportI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def deliver(self):
        raise NotImplementedError


class RoadTransport(TransportI):
    def deliver(self):
        print('Truck deliver.')


class SeaTransport(TransportI):
    def deliver(self):
        print('Sea Deliver.')


class AirPlanTransport(TransportI):
    def deliver(self):
        print('AirPlan truck.')
