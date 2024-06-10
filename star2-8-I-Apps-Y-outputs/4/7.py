
n = int(input())
a = list(map(int, input().split()))
a.sort()
x = sum(a[:n//2])
y = sum(a[n//2:])
print(abs(x - y))

