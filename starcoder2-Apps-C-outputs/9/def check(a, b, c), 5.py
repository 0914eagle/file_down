
from itertools import permutations

def check(a, b, c):
    if a > b:
        return False
    if len(set(str(a) + str(b) + str(c))) != len(str(a) + str(b) + str(c)):
        return False
    return True

def solve(n):
    ans = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if check(i, j, n):
                ans.append([i, j])
    return ans

n = int(input())
ans = solve(n)
print(len(ans))
for a, b in ans:
    print(a, b)
