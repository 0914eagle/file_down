
import sys
sys.setrecursionlimit(10000)

def solve(n, q, ops):
    if n == 1:
        return 1
    else:
        res = 0
        for op in ops:
            if op[0] in ops:
                res += solve(n - 1, q, ops - set([op]))
        return res
    
n, q = map(int, input().split())
ops = set([input()[:2] for i in range(q)])
print(solve(n, q, ops))

