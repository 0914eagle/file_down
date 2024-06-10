
n = int(input())
a = list(map(int, input().split()))

a.sort()
print(max(a[-1] - a[0], a[-2] - a[1]))

