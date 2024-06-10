
def f(n):
    return len(str(n))

def solve(S):
    res = 0
    for l in range(1, 10**8 + 1):
        r = l
        while f(r) < S:
            r += 1
        if f(r) == S:
            res += 1
    return res % (10**9 + 7)

S = int(input())
print(solve(S))

