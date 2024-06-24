# temp_inheritance\main.py

import matherator

# result = matherator.add(1, 2)
# print("Math 'Add' result:", result)


# def add(first_wun, second_wun):
#     return f"{first_wun} + {second_wun}"


# result = add(1, 2)
# print("String 'Add' result:", result)

# adder = matherator.Adder(1, 2)
# result = adder.add()
# print("Adder 'Add' result:", result)


class StringAdder(matherator.Adder):

    def __init__(self, first_wun, second_wun):
        super().__init__(first_wun, second_wun)

    def add(self):
        return f"{self.first_wun} + {self.second_wun}"

    def do_super_add(self):
        return super().add()


string_adder = StringAdder(1, 2)
print("StringAdder(1,2)")
result = string_adder.add()
print("StringAdder 'add' result:", result)

result = string_adder.do_super_add()
print("StringAdder 'do_super_add' result:", result)


list_comprehension_0_through_11 = [num for num in range(12)]
print("list_comprehension_0_through_11", list_comprehension_0_through_11)

generator_0_through_11 = (num for num in range(12))
print("dir(): ", dir())
print("dir(generator_0_through_11): ", dir(generator_0_through_11))
print("generator_0_through_11:", generator_0_through_11)
