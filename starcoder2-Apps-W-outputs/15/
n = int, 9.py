
n = int(input())
a = list(map(int, input().split()))
a.sort()
if n == 1:
    print(1)
    print(a[0])
else:
    print(2)
    print(a[0], a[n - 1])
