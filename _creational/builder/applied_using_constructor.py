class House:
    def __init__(
        self,
        windows,
        doors,
        wall,
        swimming_pool=None,
        statues=None,
        garden=None,
        garage=None,
    ) -> None:
        self.windows = windows
        self.doors = doors
        self.swimming_pool = swimming_pool
        self.statues = statues
        self.garden = garden
        self.garage = garage

    def build(self):
        self.make_doors()
        self.make_wall()
        self.make_windows()

        if self.swimming_pool:
            self.build_swimming_pool()

        if self.statues:
            self.build_statues()

        if self.garage:
            self.build_garage()

        if self.garden:
            self.build_garden()

    def make_windows(self):
        pass

    def make_wall(self):
        pass

    def make_doors(self):
        pass

    def build_garden(self):
        pass

    def build_garage(self):
        pass

    def build_swimming_pool(self):
        pass

    def build_statues(self):
        pass
