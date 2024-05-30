
def check_equivalence(str1, str2):
    if str1 == str2:
        return True
    if sorted(str1) != sorted(str2):
        return False
    half = len(str1) // 2
    a1, a2 = str1[:half], str1[half:]
    b1, b2 = str2[:half], str2[half:]
    if (check_equivalence(a1, b1) and check_equivalence(a2, b2)) or (check_equivalence(a1, b2) and check_equivalence(a2, b1)):
        return True
    return False

input_str1 = input().strip()
input_str2 = input().strip()

if check_equivalence(input_str1, input_str2):
    print("YES")
else:
    print("NO")
```
