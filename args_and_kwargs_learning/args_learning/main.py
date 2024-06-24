# Python module to learn about python `args`

first_arg_under_interest = "First Argument Under Interest"
second_arg_under_interest = "Second Argument Under Interest"  # Arg types can be mixed. Depending on the logic, any type can be passed as an argument.


def print_some_args(*args):
    print("type(args): ", type(args))
    print("args: ", args)


print_some_args(first_arg_under_interest, second_arg_under_interest)


def print_arg_in_args(*args):
    for arg in args:
        print("type(arg): ", type(arg))
        print("arg: ", arg)


print_arg_in_args(first_arg_under_interest, second_arg_under_interest)

second_arg_under_interest = 17  # Arg types can be mixed. Depending on the logic, any type can be passed as an argument.

print_some_args(first_arg_under_interest, second_arg_under_interest)
print_arg_in_args(first_arg_under_interest, second_arg_under_interest)
