
n = int(input())
f = list(map(int, input().split()))

def solve(f):
    n = len(f)
    ans = [0] * n
    for i in range(n):
        if f[i] == 0:
            for j in range(1, n + 1):
                if j not in f and j != i + 1:
                    ans[i] = j
                    break
    return ans

ans = solve(f)
print(' '.join(map(str, ans)))

