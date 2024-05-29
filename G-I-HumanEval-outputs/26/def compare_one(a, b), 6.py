
def compare_one(a, b):
    if isinstance(a, str):
        a = a.replace(',', '.')
    if isinstance(b, str):
        b = b.replace(',', '.')
    
    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b

# Test cases
print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3"
print(compare_one("5,1", "6"))  # ➞ "6"
print(compare_one("1", 1))  # ➞ None
```
