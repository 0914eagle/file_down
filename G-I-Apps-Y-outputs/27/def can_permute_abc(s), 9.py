
def can_permute_abc(s):
    if set(s) == {'a', 'b', 'c'}:
        return "Yes"
    else:
        return "No"

S = input().strip()
print(can_permute_abc(S))
```
