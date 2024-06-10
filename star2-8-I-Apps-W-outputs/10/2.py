
n = int(input())
a = [int(x) for x in input().split()]
a = sorted(a)
first = sum(a[:n//2])
second = sum(a[n//2:])
print(abs(first - second))

