
q = int(input())
for _ in range(q):
    n, a, b = map(int, input().split())
    if a < 2*b:
        print(a*n)
    else:
        print(b*n + (n//2)*b)

