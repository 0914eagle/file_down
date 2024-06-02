
n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(1, a[1] - a[0])
else:
    print(sum(a) - n * min(a), min(a))

