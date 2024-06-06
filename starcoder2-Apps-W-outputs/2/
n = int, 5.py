
n = int(input())
a = list(map(int, input().split()))
a.sort()

if n == 2:
    print(2)
else:
    i = 0
    while i < n-2 and a[i] + a[i+1] > a[i+2]:
        i += 1
    print(i+3)
