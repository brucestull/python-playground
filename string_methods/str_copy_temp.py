sample_string = "sample string"
print("sample_string: ", sample_string)  # sample string
sample_string_copy = sample_string
print("sample_string_copy: ", sample_string_copy)  # sample string

sample_string_copy = "new sample string"
print("sample_string: ", sample_string)  # sample string
print("sample_string_copy: ", sample_string_copy)  # new sample string

# The string object is mutable, so the assignment operator (=) creates a reference to the original string object.
sample_string_copy = sample_string
sample_string = "totally new sample string"
print("sample_string: ", sample_string)  # totally new sample string
print("sample_string_copy: ", sample_string_copy)  # sample string
