import datetime
import typing
import abc

# Before


class ItemA:
    def __init__(self, weight: float, price: float) -> None:
        self.weight = weight
        self.price = price


class OrderA:
    def __init__(self, line_items: typing.Iterable[ItemA], shipping) -> None:
        default = "ground"
        self.__valid_types = ["ground", "air"]
        self.__line_items = line_items
        self.__shipping_type = default
        self.__date = datetime.datetime.now().date()

    def get_total(self) -> float:
        return sum([item.price for item in self.__line_items])

    def get_total_weight(self) -> float:
        return sum([item.weight for item in self.__line_items])

    @property
    def shipping_type(self):
        return self.__shipping_type

    @shipping_type.setter
    def shipping_type(self, type: str):
        if type not in self.__valid_types:
            raise ValueError("Necessário passar um tipo válido!")
        self.__shipping_type = type

    def get_shipping_coast(self):
        if self.shipping_type == "ground":
            if self.get_total() > 100:
                return 0
            return max(10, self.get_total_weight() * 1.5)

        if self.shipping_type == "air":
            return max(20, self.get_total_weight() * 3)

    @property
    def shipping_date(self):
        return self.__date


# after - with strategy pattern


class Item:
    def __init__(self, weight: float, price: float) -> None:
        self.weight = weight
        self.price = price


class Order:
    def __init__(self, line_items: typing.Iterable[ItemA]) -> None:
        self.__line_items = line_items

    def get_total(self) -> float:
        return sum([item.price for item in self.__line_items])

    def get_total_weight(self) -> float:
        return sum([item.weight for item in self.__line_items])


class Shipping(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def date(cls):
        raise NotImplementedError

    @abc.abstractmethod
    def get_coast(cls, order: Order):
        raise NotImplementedError


class Ground(Shipping):
    def date(self):
        return "date"

    def get_coast(self, order: Order):
        if order.get_total() > 100:
            return 0
        return max(10, order.get_total_weight() * 1.5)


class Air(Shipping):
    def date(self):
        return "date"

    def get_coast(self, order: Order):
        if order.get_total() > 100:
            return 0
        return max(10, order.get_total_weight() * 1.5)
