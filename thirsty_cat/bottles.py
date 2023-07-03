class Bottle:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_volume = 0

    def fill(self, amount):
        if self.current_volume + amount > self.capacity:
            raise ValueError("Too much liquid!")
        self.current_volume += amount

    def empty(self):
        self.current_volume = 0

    def __str__(self):
        return f"{self.current_volume}/{self.capacity}"


class PopBottle(Bottle):
    def __init__(self, capacity, flavor, brand):
        super().__init__(capacity)
        self.flavor = flavor
        self.brand = brand

    def __str__(self):
        return f"{self.brand} {self.flavor} {super().__str__()}"


class BeerBottle(Bottle):
    def __init__(self, capacity, flavor, brand):
        super().__init__(capacity)
        self.flavor = flavor
        self.brand = brand

    def __str__(self):
        return f"{self.brand} {self.flavor} {super().__str__()}"
