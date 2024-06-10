
t = int(input())
a = list(map(int, input().split()))

if 0 not in a:
    print(-1)
else:
    zero_idx = a.index(0)
    n = 1
    while n * n <= zero_idx:
        n += 1
    
    m = zero_idx // n + 1
    
    x = zero_idx // m + 1
    y = zero_idx % m + 1
    
    print(n, m)
    print(x, y)

