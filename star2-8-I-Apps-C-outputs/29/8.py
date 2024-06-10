
MOD = 998244353

def solve(n):
    return (MOD + 1) // 2

n = int(input())
print(*[solve(n) % MOD for _ in range(n)], sep="\n")

