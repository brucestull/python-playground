#

# *__, a, b, *_ = [1, 2, 3, 4, 5, 6]
# print(__, _)

# SyntaxError: multiple starred expressions in assignment

*_, a = [1, 2, 3, 4, 5, 6]
print("_: ", _)
print("a: ", a)

*_, a, b = [1, 2, 3, 4, 5, 6]
print("_: ", _)
print("a: ", a)
print("b: ", b)

*_, a, b, c = [1, 2, 3, 4, 5, 6]
print("_: ", _)
print("a: ", a)
print("b: ", b)
print("c: ", c)
