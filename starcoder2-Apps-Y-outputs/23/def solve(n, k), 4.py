
def solve(n, k):
    return n * k - n + 1

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))

