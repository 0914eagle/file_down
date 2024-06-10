
n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

days = 0
solved = 0
for i in range(n):
    if solved + a[i] <= i + 1:
        solved += a[i]
        days += 1
    else:
        break

print(days)

