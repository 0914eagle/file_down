
def check_dict_case(dictionary):
    if not dictionary:
        return False
    
    upper_case_keys = all(key.isupper() for key in dictionary if isinstance(key, str))
    lower_case_keys = all(key.islower() for key in dictionary if isinstance(key, str))
    
    return upper_case_keys or lower_case_keys
