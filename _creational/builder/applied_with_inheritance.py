class House:
    def __init__(self) -> None:
        pass

    def make_windows(self):
        pass

    def make_wall(self):
        pass

    def make_doors(self):
        pass


class HouseWithGarden(House):
    def build_garden(self):
        pass


class HouseWithGarage(House):
    def build_garage(self):
        pass


class HouseWithSwimmingPool(House):
    def build_swimming_pool(self):
        pass


class HouseWithStatues(House):
    def build_statues(self):
        pass


class HouseWithStatuesAndPool(HouseWithStatues, HouseWithSwimmingPool):
    def __init__(self) -> None:
        super().__init__()
