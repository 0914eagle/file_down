
n, m = map(int, input().split())
a = list(map(int, input().split()))

a = [i for i in a if a.count(i) >= n]
if len(a) == 0:
    print(0)
else:
    print(a[0])
