
def f(n):
    return len(str(n))
def solve(S):
    count = 0
    for l in range(1, 10**8 + 1):
        r = l
        while f(r) <= S:
            if f(r) == S:
                count += 1
            r += 1
    return count % (10**9 + 7)
S = int(input())
print(solve(S))

