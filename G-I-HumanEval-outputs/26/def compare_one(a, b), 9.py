
def compare_one(a, b):
    if type(a) != type(b):
        return max(a, b)
    
    if isinstance(a, str):
        a = a.replace(',', '.')
        b = b.replace(',', '.')
    
    if float(a) > float(b):
        return a
    elif float(b) > float(a):
        return b
    else:
        return None

# Test cases
print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3"
print(compare_one("5,1", "6"))  # ➞ "6"
print(compare_one("1", 1))  # ➞ None
```
