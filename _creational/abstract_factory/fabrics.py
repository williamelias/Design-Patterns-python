import abc

from .products import (
    ModernSofa,
    VictorianSofa,
    Sofa,
    Table,
    ModernChair,
    ModernTable,
    Chair,
    VictorianChair,
    VictorianTable
)


class Forniture(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_sofa(self) -> Sofa:
        raise NotImplementedError

    @abc.abstractmethod
    def create_table(self) -> Table:
        raise NotImplementedError

    @abc.abstractmethod
    def create_chair(self) -> Chair:
        raise NotImplementedError


class ModernForniture(Forniture):
    def create_chair(self) -> ModernChair:
        return ModernChair()

    def create_sofa(self) -> ModernSofa:
        return ModernSofa()

    def create_table(self) -> ModernTable:
        return ModernTable()


class VictorianForniture(Forniture):
    def create_chair(self) -> VictorianChair:
        return VictorianChair()

    def create_sofa(self) -> VictorianSofa:
        return VictorianSofa()

    def create_table(self) -> VictorianTable:
        return VictorianTable()
