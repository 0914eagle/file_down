
def f(n):
    return len(str(n))
def solve(S):
    ans = 0
    for l in range(1, 10**8 + 1):
        r = l
        while f(r) < S:
            r += 1
        if f(r) == S:
            ans += 1
    return ans % (10**9 + 7)
S = int(input())
print(solve(S))

