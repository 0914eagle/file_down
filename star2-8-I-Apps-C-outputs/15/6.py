
n = int(input())
a = list(map(int, input().split()))

if all(i == 0 for i in a):
    print(-1)
else:
    gcd = a[0]
    for i in range(1, n):
        gcd = math.gcd(gcd, a[i])
    
    print(gcd - 1)

