class Animal:
    def __init__(self, name):
        self.name = name
        self.has_mobility = True

    def sound_off(self):
        pass


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.has_fur = True


class Cat(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def sound_off(self):
        return f"Meow, I'm {self.name}."


class Human(Mammal):
    def __init__(self, name):
        super().__init__(name)
        self.has_spoken_language = True

    def sound_off(self):
        return f"Hello, I'm {self.name}."
