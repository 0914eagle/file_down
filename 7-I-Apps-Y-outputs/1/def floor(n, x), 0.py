
def floor(n, x):
    if n <= 2:
        return 1
    return 1 + (n - 2) // x

t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    print(floor(n, x))

