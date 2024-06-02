
d, n = map(int, input().split())

if d == 0:
    print(n)
elif d == 1:
    print(100*n)
else:
    if n == 100:
        print(10100)
    else:
        print(100*n)

