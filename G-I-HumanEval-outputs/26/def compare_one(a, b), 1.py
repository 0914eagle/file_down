
def compare_one(a, b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return max(a, b) if a != b else None
        else:
            b = b.replace(',', '.')
            return max(a, float(b)) if a != float(b) else None
    else:
        if type(b) == int or type(b) == float:
            a = a.replace(',', '.')
            return max(float(a), b) if float(a) != b else None
        else:
            a = a.replace(',', '.')
            b = b.replace(',', '.')
            return b if a == b else max(a,b)

# Test cases
print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3"
print(compare_one("5,1", "6"))  # ➞ "6"
print(compare_one("1", 1))  # ➞ None
```
