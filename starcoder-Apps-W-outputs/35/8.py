
for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    s = sum(x)
    x.sort()
    a = x[-1]
    for i in range(n - 1):
        s -= x[i]
        if x[i] > 0:
            a = max(a, x[i] * (s // (i + 1)))
    print(a)
