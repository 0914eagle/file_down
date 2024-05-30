
def find_x(n):
    x = 1
    while n % (2*x - 1) != 0:
        x += 1
    return x

t = int(input())
for _ in range(t):
    n = int(input())
    x = find_x(n)
    print(x)
