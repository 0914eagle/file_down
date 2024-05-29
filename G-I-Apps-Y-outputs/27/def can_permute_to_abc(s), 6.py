
def can_permute_to_abc(s):
    return set(s) == set('abc')

S = input()
if can_permute_to_abc(S):
    print('Yes')
else:
    print('No')
