
n = int(input())
a = list(map(int, input().split()))
a.sort()
snuke = sum(a[:n//2])
raccoon = sum(a[n//2:])
print(abs(snuke - raccoon))

