
 def check_dict_case(dict):
    if len(dict) == 0:
        return False
    else:
        for key in dict:
            if type(key) != str:
                return False
            else:
                if key.islower() or key.isupper():
                    continue
                else:
                    return False
        return True
 