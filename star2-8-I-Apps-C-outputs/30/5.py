
def solve(n, q, ops):
    if n == 1:
        return 1
    if q == 0:
        return 0
    
    cnt = 0
    for i in range(q):
        a, b = ops[i]
        if n >= 2 and a[0] == b:
            cnt += solve(n-1, q-1, ops[:i]+ops[i+1:])
        if n >= 2 and a[1] == b:
            cnt += solve(n-1, q-1, ops[:i]+ops[i+1:])
            
    return cnt


n, q = map(int, input().split())
ops = [input().split() for _ in range(q)]
print(solve(n, q, ops))

