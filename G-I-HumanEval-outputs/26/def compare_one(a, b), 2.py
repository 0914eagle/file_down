
def compare_one(a, b):
    def extract_number(val):
        if isinstance(val, int) or isinstance(val, float):
            return val
        else:  # val is a string
            val = val.replace(',', '.')  # handle comma-separated numbers
            return float(val)

    a_num = extract_number(a)
    b_num = extract_number(b)

    if a_num > b_num:
        return a
    elif a_num < b_num:
        return b
    else:
        return None

# Test cases
print(compare_one(1, 2.5))  # Output should be 2.5
print(compare_one(1, "2,3"))  # Output should be "2,3"
print(compare_one("5,1", "6"))  # Output should be "6"
print(compare_one("1", 1))  # Output should be None
```
