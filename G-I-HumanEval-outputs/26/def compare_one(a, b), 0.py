
def compare_one(a, b):
    if type(a) == type(b):
        if isinstance(a, int) or isinstance(a, float):
            return max(a, b) if a != b else None
        elif isinstance(a, str):
            a_val = float(a.replace(',', '.')) if ',' in a else float(a)
            b_val = float(b.replace(',', '.')) if ',' in b else float(b)
            return str(max(a_val, b_val)) if a_val != b_val else None
    else:
        return max(a, b)

# Test cases
print(compare_one(1, 2.5)) # ➞ 2.5
print(compare_one(1, "2,3")) # ➞ "2,3"
print(compare_one("5,1", "6")) # ➞ "6"
print(compare_one("1", 1)) # ➞ None
```
