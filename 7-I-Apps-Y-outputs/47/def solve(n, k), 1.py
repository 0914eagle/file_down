
def solve(n, k):
    for i in range(1, n+1):
        if n % i == 0:
            return i
    return 1

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))

