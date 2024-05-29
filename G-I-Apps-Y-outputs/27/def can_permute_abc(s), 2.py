
def can_permute_abc(s):
    sorted_str = ''.join(sorted(s))
    return sorted_str == 'abc'

S = input().strip()
if can_permute_abc(S):
    print("Yes")
else:
    print("No")
```
