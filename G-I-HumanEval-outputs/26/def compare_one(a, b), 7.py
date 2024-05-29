
def compare_one(a, b):
    if type(a) != type(b):
        return max(a, b)
    elif type(a) == int or type(a) == float:
        return max(a, b) if a != b else None
    elif isinstance(a, str) and isinstance(b, str):
        a_num = float(a.replace(',', '.')) if ',' in a else float(a)
        b_num = float(b.replace(',', '.')) if ',' in b else float(b)
        return b if a_num <= b_num else a
    else:
        return None

# Test cases
print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3"
print(compare_one("5,1", "6"))  # ➞ "6"
print(compare_one("1", 1))  # ➞ None
```
