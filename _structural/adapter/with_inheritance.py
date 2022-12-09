# Exemplo tirado do pseudocódigo do livro de embasamento desse estudo
import math


class RoundPeg:
    def __init__(self, radius: int) -> None:
        self.__radius = radius

    def get_radius(self):
        return self.__radius


# Classe incompatível


class SquarePeg:
    def __init__(self, width: int) -> None:
        self.__width = width

    def get_width(self):
        return self.__width


# Adapter
class SquarePegAdapter(RoundPeg):
    def __init__(self, peg: SquarePeg) -> None:
        self.__peg = peg
        self.sqrt_divided = math.sqrt(2) / 2

    def get_radius(self):
        return self.__peg.get_width() * self.sqrt_divided


# Classe já existente
class RoundHole:
    def __init__(self, radius: int) -> None:
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def fits(self, peg: RoundPeg):
        return self.get_radius() >= peg.get_radius()


"""
Exemplo de uso 1 (com a classe compatível):

    peg = RoundPeg(10)

    hole = RoundHole(10)

    hole.fits(peg=peg)

Exemplo de uso 2 (com a classe incompatível e adapter):

    square_peg = SquarePeg(12)

    hole = RoundHole(10)

    hole.fits(peg=square_peg)

"""
