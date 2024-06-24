prices = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = 0.08


def get_price_with_tax(price):
    return price * (1 + TAX_RATE)


final_prices = map(get_price_with_tax, prices)
final_prices
print("final_prices: ", list(final_prices))


def square_a_thing(x):
    return x * x


squared = map(square_a_thing, [1, 2, 3, 4, 5])
print("squared: ", list(squared))


def plus_three_things(x, y, z):
    return x + y + z


the_result = map(plus_three_things, [1, 2, 3], [4, 5, 6], [7, 8, 9])
print("the_result: ", list(the_result))

the_result = map(plus_three_things, [1, 2, 3], [4, 5, 6], [7, 8])
print("the_result: ", list(the_result))
