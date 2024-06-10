
N = int(input())
a = [int(i) for i in input().split()]
a.sort()

x = sum(a[:N//2])
y = sum(a[N//2:])
print(abs(x-y))

