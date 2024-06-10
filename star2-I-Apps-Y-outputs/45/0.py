
q = int(input())
for i in range(q):
    n, a, b = map(int, input().split())
    if a < 2*b:
        print(a*n)
    else:
        print(b*(n//2)*2 + a*(n%2))

