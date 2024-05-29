
def compare_one(a, b):
    if a == b:
        return None

    a_type = type(a)
    b_type = type(b)

    if a_type == b_type:
        if a_type == int or a_type == float:
            return max(a, b)
        else:
            if ',' in a:
                a = a.replace(',', '.')
            if ',' in b:
                b = b.replace(',', '.')
            return max(float(a), float(b))
    else:
        if a_type == int or a_type == float:
            if b_type == str:
                if ',' in b:
                    b = b.replace(',', '.')
                return max(a, float(b))
            else:
                return a
        else:
            if ',' in a:
                a = a.replace(',', '.')
            if b_type == int or b_type == float:
                return max(float(a), b)
            elif ',' in b:
                b = b.replace(',', '.')
                return max(float(a), float(b))

# Test cases
print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3" 
print(compare_one("5,1", "6"))  # ➞ "6"
print(compare_one("1", 1))  # ➞ None
```
