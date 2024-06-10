
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x = 0
    y = sum(a)
    min_diff = abs(x-y)
    for i in range(n-1):
        x += a[i]
        y -= a[i]
        min_diff = min(min_diff, abs(x-y))
    
    print(min_diff)

solve()

