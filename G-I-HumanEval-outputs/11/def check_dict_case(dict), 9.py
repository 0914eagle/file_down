
def check_dict_case(dict):
    if not dict:
        return False
    
    lowercase_keys = all(key.islower() for key in dict if isinstance(key, str))
    uppercase_keys = all(key.isupper() for key in dict if isinstance(key, str))
    
    return lowercase_keys or uppercase_keys
