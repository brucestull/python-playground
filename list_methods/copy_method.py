# list_methods\copy_method.py

# Create a list:
nums = [1, 2, 3, 4, 5]

# # Print the list:
# print("nums: ", nums)

# # Create a lambda function that multiplies a number by 2:
# multiply_by_2 = lambda x: x * 2

# # Use the lambda function to multiply each number in the list by 2:
# doubled_nums = list(map(multiply_by_2, nums))
# print("doubled_nums: ", doubled_nums)

# This statement creates another reference to the list:
# The new name `nums_1` is a reference to the same list object as `nums`.
print("The new name `nums_1` is a reference to the same list object as `nums`.")
nums_1 = nums
print("nums_1 = nums")
print("nums: ", nums)
print("nums_1: ", nums_1)

# Change the first element of the list, via the new reference:
nums_1[0] = 10
print("nums_1[0] = 10")
# The change is reflected in the original list:
print("nums: ", nums)
print("nums_1: ", nums_1)

# Create a shallow copy of the list:
# The new name `nums_2` is a reference to a new list object that contains the same elements as `nums`.
print(
    "The new name `nums_2` is a reference to a new list object that contains the same elements as `nums`."
)
nums_2 = nums.copy()
print("nums_2 = nums.copy()")
print("nums: ", nums)
print("nums_2: ", nums_2)

# Change the first element of the list, via the new reference:
nums_2[0] = 100
print("nums_2[0] = 100")
# The change is not reflected in the original list:
print("The change is not reflected in the original list:")
print("nums: ", nums)
print("nums_2: ", nums_2)
