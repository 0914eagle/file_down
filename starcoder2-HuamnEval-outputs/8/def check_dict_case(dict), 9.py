
def check_dict_case(dict):
    if len(dict) == 0:
        return False
    else:
        if all(isinstance(key, str) for key in dict):
            if all(key.islower() for key in dict) or all(key.isupper() for key in dict):
                return True
            else:
                return False
        else:
            return False
 