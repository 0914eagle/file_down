
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
days = 0
for i in range(n):
    days += 1
    if a[i] < days:
        break
print(days)

