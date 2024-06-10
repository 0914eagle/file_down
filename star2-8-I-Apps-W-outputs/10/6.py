
n = int(input())
a = list(map(int, input().split()))
a.sort()
a = [360 - i for i in a]
sum1 = 0
sum2 = sum(a)
diff = abs(sum1 - sum2)
for i in range(n):
    sum1 += a[i]
    sum2 -= a[i]
    diff = min(diff, abs(sum1 - sum2))
print(diff)

