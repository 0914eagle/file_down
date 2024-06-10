
def solve(a):
    n = len(a)
    m = 1
    while n * m != len(a):
        m += 1
    x = 0
    y = 0
    for i in range(n):
        for j in range(m):
            if a[i * m + j] == 0:
                x = i + 1
                y = j + 1
    if x == 0:
        return -1
    return f"{n} {m}\n{x} {y}"

t = int(input())
a = list(map(int, input().split()))
print(solve(a))

