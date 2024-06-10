
def f(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i

def solve(n, k):
    for _ in range(k):
        n += f(n)
    return n

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))

