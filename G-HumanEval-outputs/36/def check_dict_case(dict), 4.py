
def check_dict_case(dict):
    if not dict:
        return False
    
    lowercase_keys = all(isinstance(key, str) and key.islower() for key in dict.keys())
    uppercase_keys = all(isinstance(key, str) and key.isupper() for key in dict.keys())
    
    return lowercase_keys or uppercase_keys
