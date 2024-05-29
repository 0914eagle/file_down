
def can_permute_abc(s):
    return set(s) == set('abc')

S = input().strip()
if can_permute_abc(S):
    print("Yes")
else:
    print("No")
```
