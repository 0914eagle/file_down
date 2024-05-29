
def check_dict_case(dictionary):
    if not dictionary:
        return False
    
    keys = list(dictionary.keys())
    
    lower_case = all(key.islower() for key in keys if isinstance(key, str))
    upper_case = all(key.isupper() for key in keys if isinstance(key, str))
    
    return lower_case or upper_case

# Testing the function with provided examples
print(check_dict_case({"a": "apple", "b": "banana"}))  # True
print(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))  # False
print(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))  # False
print(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))  # False
print(check_dict_case({"STATE": "NC", "ZIP": "12345"}))  # True
