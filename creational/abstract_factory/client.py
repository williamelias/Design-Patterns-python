from fabrics import Forniture


class Client:
    def __init__(self, forniture: Forniture) -> None:
        self.__forniture = forniture

    def furnish(self):
        self.__forniture.create_chair()
        self.__forniture.create_sofa()
        self.__forniture.create_table()
