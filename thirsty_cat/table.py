from bottles import PopBottle, BeerBottle


class Table:
    def __init__(self, bottles):
        self.bottles = bottles

    def fill(self, amount):
        for bottle in self.bottles:
            bottle.fill(amount)

    def empty(self):
        for bottle in self.bottles:
            bottle.empty()

    def __str__(self):
        return "\n".join([str(bottle) for bottle in self.bottles])


def main():
    pop_1 = PopBottle(200, "cola", "Coca-Cola")
    beer_1 = BeerBottle(100, "lager", "Budweiser")

    table = Table([pop_1, beer_1])
    print(table)

    pop_1.fill(100)
    beer_1.fill(50)
    print(table)


if __name__ == "__main__":
    main()
