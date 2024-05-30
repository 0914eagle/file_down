
def floor(n, x):
    if n <= 2:
        return 1
    else:
        return (n // 2) + 1

t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    print(floor(n, x))

