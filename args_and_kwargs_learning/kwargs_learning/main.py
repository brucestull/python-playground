# Python module to learn about python `kwargs`


first_keyword_argument_under_interest = "First Keyword Argument Under Interest"
second_keyword_argument_under_interest = 17  # Arg types can be mixed. Depending on the logic, any type can be passed as an argument.
second_keyword_argument_under_interest = "Second Keyword Argument Under Interest"  # Arg types can be mixed. Depending on the logic, any type can be passed as an argument.


def print_kwargs(**kwargs):
    print("type(kwargs): ", type(kwargs))
    print("kwargs: ", kwargs)


kwargs_under_interest = {
    "first_kwarg_under_interest": first_keyword_argument_under_interest,
    "second_kwarg_under_interest": second_keyword_argument_under_interest,
}

print_kwargs(**kwargs_under_interest)


def print_kwarg_in_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("type(value): ", type(value))
        print(f"{key}: {value}")


print_kwarg_in_kwargs(**kwargs_under_interest)
