print(f"__name__ is '{__name__}' in 'table.py'")

from bottles import PopBottle, BeerBottle


class Table:
    """
    Class representing a table with bottles on it.

    Attributes:
        bottles (list): List of bottles on the table.

    Methods:
        fill: Adds liquid to all bottles on the table.
        empty: Empties all bottles on the table.
    """

    def __init__(self, bottles):
        self.bottles = bottles

    def fill(self, amount):
        """
        Method for adding liquid to all bottles on the table.
        """
        for bottle in self.bottles:
            bottle.fill(amount)

    def empty(self):
        """
        Method for emptying all bottles on the table.
        """
        for bottle in self.bottles:
            bottle.empty()

    def __str__(self):
        """
        String representation of the table.
        """
        # We are using a list comprehension here. This is a way to create a list.
        # We are using the join method with a newline character to create a string. This will return the individual bottles as a string separated by a newline character. If we added a newline character to the end of the string, we would have an extra newline character at the end of the string.
        return "\n".join([str(bottle) for bottle in self.bottles])


def main():
    """
    We are using a `main` method to run our code. This is a common practice in Python. This allows us to import this file without running the code. This is useful if we want to use the classes in this file in another file.
    """
    # We are creating two bottles.
    pop_1 = PopBottle(200, "100%", "Coca-Cola")
    beer_1 = BeerBottle(100, "5.1%", "Budweiser")

    # We are creating a table with the two bottles.
    table = Table([pop_1, beer_1])
    print(table)

    # We are filling each of the individual the bottles on the table. If we used the `fill` method on the table, we would fill both bottles with the same amount.
    pop_1.fill(100)
    beer_1.fill(50)
    print(table)

    pop_1.drink(50)
    beer_1.drink(25)
    print(table)

# We are checking if the file is being run directly. If it is, we run the `main` method.
# ¿`__name__` will be equal to `"__main__"` if the file is being run directly. If the file is being imported, `__name__` will be equal to the name of the file?
if __name__ == "__main__":
    main()
