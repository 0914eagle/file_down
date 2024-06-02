
def check_dict_case(dict):
    if not dict:
        return False
    lower_keys = [key.lower() for key in dict.keys()]
    upper_keys = [key.upper() for key in dict.keys()]
    return lower_keys == list(dict.keys()) or upper_keys == list(dict.keys())
 