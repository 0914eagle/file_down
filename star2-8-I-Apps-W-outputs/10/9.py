
n = int(input())
a = list(map(int, input().split()))
a.sort()
summ = 0
for i in range(n):
    summ += a[i]
    if summ >= 180:
        print(abs(summ - 360 + summ - 360))
        break

