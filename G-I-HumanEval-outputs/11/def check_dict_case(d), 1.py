
def check_dict_case(d):
    if not d:  # Check if dictionary is empty
        return False

    lower_keys = all(isinstance(key, str) and key.islower() for key in d.keys())
    upper_keys = all(isinstance(key, str) and key.isupper() for key in d.keys())

    return lower_keys or upper_keys

# Test cases
print(check_dict_case({"a":"apple", "b":"banana"}))  # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))  # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))  # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))  # True
