print(f"__name__ is '{__name__}' in 'bottles.py'")

class Bottle:
    """
    Class representing a bottle.

    Attributes:
        capacity (int): The maximum volume of the bottle.
        liquid_unit (str): The unit of measurement for the capacity and volume.
        current_volume (int): The current volume of the bottle.

    Methods:
        fill: Adds liquid to the bottle.
        empty: Empties the bottle.
    """

    def __init__(self, capacity, liquid_unit="ml"):
        """
        The constructor for the Bottle class.

        Default the capacity unit to milliliters (ml).

        Parameters:
            capacity (int): The maximum volume of the bottle.
            liquid_unit (str): The unit of measurement for the capacity and volume.
            current_volume (int): The current volume of liquid the bottle.
        """
        self.capacity = capacity
        self.liquid_unit = liquid_unit
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

    def drink(self, amount):
        """
        Method for drinking liquid from the bottle.

        This method is not implemented in the Bottle class. This method will be implemented in the PopBottle and BeerBottle classes.

        This is an example of a method that is not implemented in the parent class. This method will be implemented in the child classes. This is an example of polymorphism. Polymorphism is the ability to use the same interface for different data types. In this case, we are using the same interface (the drink method) for different data types (PopBottle and BeerBottle).
        """
        pass

    def __str__(self):
        return f"{self.current_volume}/{self.capacity}"


class PopBottle(Bottle):
    """
    Class representing a pop bottle. This class inherits from the Bottle class.

    Attributes:
        capacity (int) [from super class]: The maximum volume of the bottle.
        caffeine_content (str): The caffeine content of the pop.
        brand (str): The brand of the pop.

    Methods:
        fill [from super class]: Adds liquid to the bottle.
        empty [from super class]: Empties the bottle.
    """

    def __init__(self, capacity, caffeine_content, brand):
        super().__init__(capacity)
        self.caffeine_content = caffeine_content
        self.brand = brand

    def drink(self, amount):
        """
        Method for drinking liquid from the PopBottle.

        This method is overridden from the Bottle class. This is an example of polymorphism. Polymorphism is the ability to use the same interface for different data types. In this case, we are using the same interface (the drink method) for different data types (PopBottle and BeerBottle).
        """
        if self.current_volume - amount < 0:
            raise ValueError("Not enough liquid!")
        self.current_volume -= amount
        print("Chugging the ", self.brand, " pop!")

    def __str__(self):
        return f"{self.brand} {self.caffeine_content} {super().__str__()}"


class BeerBottle(Bottle):
    """
    Class representing a beer bottle. This class inherits from the Bottle class.

    Attributes:
        capacity (int) [from super class]: The maximum volume of the bottle.
        alcohol_content (str): The alcohol content of the beer.
        brand (str): The brand of the beer.

    Methods:
        fill [from super class]: Adds liquid to the bottle.
        empty [from super class]: Empties the bottle.
    """

    def __init__(self, capacity, alcohol_content, brand):
        super().__init__(capacity)
        self.alcohol_content = alcohol_content
        self.brand = brand

    def drink(self, amount):
        """
        Method for drinking liquid from the BeerBottle.

        This method is being overridden from the Bottle class. This is an example of polymorphism. Polymorphism is the ability to use the same interface for different data types. In this case, we are using the same interface (the drink method) for different data types (PopBottle and BeerBottle).
        """
        if self.current_volume - amount < 0:
            raise ValueError("Not enough liquid!")
        self.current_volume -= amount
        print("Choking down the ", self.brand, " beer!")

    def __str__(self):
        return f"{self.brand} {self.alcohol_content} {super().__str__()}"
