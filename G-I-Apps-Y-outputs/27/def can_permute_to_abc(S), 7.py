
def can_permute_to_abc(S):
    return 'Yes' if sorted(S) == ['a', 'b', 'c'] else 'No'

S = input().strip()
print(can_permute_to_abc(S))
```
