
n = int(input())
a = list(map(int, input().split()))
a.sort()
if len(a) == 1:
    print(1)
    print(a[0])
elif len(a) == 2:
    print(2)
    print(a[0], a[1])
else:
    if a[0] == 0:
        print(n)
        for i in range(n):
            print(a[i], end=' ')
    else:
        print(n-1)
        for i in range(n-1):
            print(a[i], end=' ')
