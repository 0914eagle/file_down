
n = int(input())
a = list(map(int, input().split()))
a.sort()
if a[0] == a[1]:
    print(n)
else:
    print(n - 1)
