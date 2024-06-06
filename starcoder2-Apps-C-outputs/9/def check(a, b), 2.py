
from itertools import permutations

def check(a, b):
    a = str(a)
    b = str(b)
    for i in a:
        if i in b:
            return False
    return True

def solve(p):
    ans = []
    for i in range(1, p):
        if check(i, p - i):
            ans.append((i, p - i))
    return ans

p = int(input())
ans = solve(p)
print(len(ans))
for a, b in ans:
    print(a, b)
