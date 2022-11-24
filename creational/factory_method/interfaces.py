import abc 


class TransportI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def deliver(self):
        raise NotImplementedError


class LogisticsI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def plan_delivery(self):
        """create a plan delivery"""
        raise NotImplementedError

    @abc.abstractmethod
    def create_transport(self)-> TransportI:
        """Create a transport vehicle"""
        raise NotImplementedError
