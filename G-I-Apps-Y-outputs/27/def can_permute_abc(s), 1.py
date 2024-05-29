
def can_permute_abc(s):
    if sorted(s) == ['a', 'b', 'c']:
        return 'Yes'
    else:
        return 'No'

# Input
s = input().strip()

# Output
print(can_permute_abc(s))
```
