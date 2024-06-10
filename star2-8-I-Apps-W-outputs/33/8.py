
from itertools import product

def solve(s1, s2):
    n = len(s1)
    valid_pos = set()
    for comb in product([0, 1], repeat=s2.count('?')):
        pos = 0
        for i in range(n):
            if s2[i] == '+':
                pos += 1
            elif s2[i] == '-':
                pos -= 1
            else: # s2[i] == '?'
                pos += comb[i] - comb[i] # comb[i] is 0 or 1, so the diff is -1 or 1
        valid_pos.add(pos)
    
    if s1[-1] == '+':
        target = 1
    else:
        target = -1
        
    return sum(pos == target for pos in valid_pos) / len(valid_pos)
    
s1 = input()
s2 = input()
print(solve(s1, s2))

