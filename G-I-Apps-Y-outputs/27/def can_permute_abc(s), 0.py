
def can_permute_abc(s):
    if s == 'abc' or s == 'acb' or s == 'bac' or s == 'bca' or s == 'cab' or s == 'cba':
        return 'Yes'
    else:
        return 'No'

# Input
s = input().strip()

# Output
print(can_permute_abc(s))
