print(f"__name__ is '{__name__}' in bottles.py")

class Bottle:
    """
    Class representing a bottle.

    Attributes:
        capacity (int): The maximum volume of the bottle.
        current_volume (int): The current volume of the bottle.

    Methods:
        fill: Adds liquid to the bottle.
        empty: Empties the bottle.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.current_volume = 0

    def fill(self, amount):
        """
        Method for adding liquid to the bottle.
        """
        if self.current_volume + amount > self.capacity:
            raise ValueError("Too much liquid!")
        self.current_volume += amount

    def empty(self):
        """
        Method for emptying the bottle.
        """
        self.current_volume = 0

    def __str__(self):
        return f"{self.current_volume}/{self.capacity}"


class PopBottle(Bottle):
    """
    Class representing a pop bottle. This class inherits from the Bottle class.

    Attributes:
        capacity (int) [from super class]: The maximum volume of the bottle.
        flavor (str): The flavor of the pop.
        brand (str): The brand of the pop.

    Methods:
        fill [from super class]: Adds liquid to the bottle.
        empty [from super class]: Empties the bottle.
    """

    def __init__(self, capacity, caffiene_content, brand):
        super().__init__(capacity)
        self.caffiene_content = caffiene_content
        self.brand = brand

    def __str__(self):
        return f"{self.brand} {self.caffiene_content} {super().__str__()}"


class BeerBottle(Bottle):
    """
    Class representing a beer bottle. This class inherits from the Bottle class.

    Attributes:
        capacity (int) [from super class]: The maximum volume of the bottle.
        flavor (str): The flavor of the beer.
        brand (str): The brand of the beer.

    Methods:
        fill [from super class]: Adds liquid to the bottle.
        empty [from super class]: Empties the bottle.
    """

    def __init__(self, capacity, alcohol_content, brand):
        super().__init__(capacity)
        self.alcohol_content = alcohol_content
        self.brand = brand

    def __str__(self):
        return f"{self.brand} {self.alcohol_content} {super().__str__()}"
