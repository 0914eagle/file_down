
def solve(n, a, b):
    pos = [0] * (n + 1)
    for i in range(n):
        pos[a[i]] = i
    ans = 0
    for i in range(n):
        if b[i] == 0:
            continue
        j = pos[b[i]]
        ans += j - i
        for k in range(j, i, -1):
            b[k] = b[k - 1]
        b[i] = b[j]
        b[j] = 0
        for k in range(n):
            if b[k] != 0:
                pos[b[k]] = k
    return ans

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, a, b))

