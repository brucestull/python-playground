# temp_inheritance\matherator.py


def add(first_wun, second_wun):
    return first_wun + second_wun


class Adder:
    def __init__(self, first_wun, second_wun):
        self.first_wun = first_wun
        self.second_wun = second_wun

    def add(self):
        return self.first_wun + self.second_wun
