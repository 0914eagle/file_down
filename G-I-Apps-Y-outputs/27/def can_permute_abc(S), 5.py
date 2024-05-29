
def can_permute_abc(S):
    if S == 'abc' or S == 'acb' or S == 'bac' or S == 'bca' or S == 'cab' or S == 'cba':
        return 'Yes'
    else:
        return 'No'

S = input().strip()
print(can_permute_abc(S))
```
