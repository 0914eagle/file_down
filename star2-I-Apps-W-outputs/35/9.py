
def solve(k, a):
    n = sum(a)
    if k > n:
        return -1
    if k == n:
        return 7
    if k == 1:
        return 1
    if n == 1:
        return 7
    return (k - 1) * (n // k) + n

t = int(input())
for _ in range(t):
    k = int(input())
    a = list(map(int, input().split()))
    print(solve(k, a))

