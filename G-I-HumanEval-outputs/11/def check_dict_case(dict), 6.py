
def check_dict_case(dict):
    if not dict:
        return False

    lowercase_keys = all(key.islower() for key in dict.keys() if isinstance(key, str))
    uppercase_keys = all(key.isupper() for key in dict.keys() if isinstance(key, str))

    return lowercase_keys or uppercase_keys

# Test cases
print(check_dict_case({"a":"apple", "b":"banana"}))  # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))  # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))  # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"}))  # True
