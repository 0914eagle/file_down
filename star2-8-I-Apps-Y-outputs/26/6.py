
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    s = input()
    r = g = b = 0
    for ch in s:
        if ch == 'R':
            r += 1
        elif ch == 'G':
            g += 1
        else:
            b += 1
    print(min(n - r, n - g, n - b))

