
 def check_dict_case(dict):
    if not dict:
        return False
    if all(isinstance(x, str) for x in dict.keys()):
        if all(x.islower() for x in dict.keys()):
            return True
        elif all(x.isupper() for x in dict.keys()):
            return True
        else:
            return False
    else:
        return False
 