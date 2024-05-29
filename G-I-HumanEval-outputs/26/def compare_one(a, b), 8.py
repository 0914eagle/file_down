
def compare_one(a, b):
    def convert_to_number(val):
        if isinstance(val, int) or isinstance(val, float):
            return val
        else:
            val = val.replace(',', '.') if isinstance(val, str) else val
            try:
                return int(val) if float(val).is_integer() else float(val)
            except ValueError:
                return val

    a_num = convert_to_number(a)
    b_num = convert_to_number(b)

    if a_num == b_num:
        return None
    elif isinstance(a_num, str) or isinstance(b_num, str):
        return str(max(a_num, b_num))
    else:
        return max(a_num, b_num)

# Test cases
print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3"
print(compare_one("5,1", "6"))  # ➞ "6"
print(compare_one("1", 1))  # ➞ None
```
