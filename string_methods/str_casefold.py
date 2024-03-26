sample_string = "sample string"
print("sample_string: ", sample_string)  # sample string
upper_case_string = sample_string.upper()
print("upper_case_string: ", upper_case_string)  # SAMPLE STRING

print(
    f"sample_string.casefold() == upper_case_string.casefold(): {sample_string.casefold() == upper_case_string.casefold()}"
)
