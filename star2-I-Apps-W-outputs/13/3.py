
def f(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    for _ in range(k):
        n += f(n)
    print(n)

