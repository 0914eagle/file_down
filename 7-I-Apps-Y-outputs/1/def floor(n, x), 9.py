
def floor(n, x):
    if n <= 2:
        return 1
    else:
        return floor(n - 2, x) + 1

t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    print(floor(n, x))

