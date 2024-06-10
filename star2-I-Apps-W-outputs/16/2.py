
def solve(a):
    n = len(a)
    if n == 1:
        return 1
    
    count = 0
    while True:
        i = 0
        while i < n - 1:
            if a[i] != a[i + 1]:
                a[i] += a[i + 1]
                del a[i + 1]
                n -= 1
                count += 1
                break
            i += 1
        if i == n - 1:
            break
    
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

