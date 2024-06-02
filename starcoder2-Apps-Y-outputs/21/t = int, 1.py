
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(k):
        a[i], b[n-i-1] = b[n-i-1], a[i]
    print(sum(a))

