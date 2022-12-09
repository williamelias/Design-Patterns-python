import abc


class Chair(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def has_legs() -> bool:
        raise NotImplementedError


class Sofa(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sit() -> str:
        raise NotImplementedError


class Table(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def max_weight() -> int:
        raise NotImplementedError


# ModernProducts


class ModernChair(Chair):
    def has_legs() -> bool:
        return True


class ModernSofa(Sofa):
    def sit() -> str:
        return 'yes'


class ModernTable(Table):
    def max_weight() -> int:
        return 100


# VictorianProducts


class VictorianChair(Chair):
    def has_legs() -> bool:
        return False


class VictorianSofa(Sofa):
    def sit() -> str:
        return 'yes or no'


class VictorianTable(Table):
    def max_weight() -> int:
        return 50
