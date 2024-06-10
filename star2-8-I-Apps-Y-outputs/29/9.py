
n = int(input())
a = list(map(int, input().split()))

a.sort()

days = 0

for i in range(n):
    if a[i] >= i+1:
        days += 1
    else:
        break

print(days)

