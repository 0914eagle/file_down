
def check_dict_case(dict):
    if not dict:
        return False
    
    lower_count = 0
    upper_count = 0
    
    for key in dict.keys():
        if isinstance(key, str):
            if key.islower():
                lower_count += 1
            elif key.isupper():
                upper_count += 1
            else:
                return False
        else:
            return False
    
    return lower_count == 0 or upper_count == 0

# Test cases
print(check_dict_case({"a": "apple", "b": "banana"})) # True
print(check_dict_case({"a": "apple", "A": "banana", "B": "banana"})) # False
print(check_dict_case({"a": "apple", 8: "banana", "a": "apple"})) # False
print(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"})) # False
print(check_dict_case({"STATE": "NC", "ZIP": "12345"})) # True
