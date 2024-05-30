
def floor(n, x):
    if n == 1:
        return 1
    else:
        return (n - 1) // x + 1

t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    print(floor(n, x))

