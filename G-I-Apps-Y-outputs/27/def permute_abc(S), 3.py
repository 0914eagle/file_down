
def permute_abc(S):
    sorted_str = ''.join(sorted(S))
    if sorted_str == 'abc':
        return 'Yes'
    else:
        return 'No'

S = input().strip()
print(permute_abc(S))
```
