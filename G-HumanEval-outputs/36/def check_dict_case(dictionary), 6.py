
def check_dict_case(dictionary):
    if not dictionary:
        return False

    upper_keys = [key for key in dictionary.keys() if str(key).isupper()]
    lower_keys = [key for key in dictionary.keys() if str(key).islower()]

    if len(upper_keys) == 0 or len(lower_keys) == 0:
        return True
    else:
        return False
```
