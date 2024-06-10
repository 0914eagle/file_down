
n = int(input())
a = list(map(int, input().split()))
days = 0
i = 0
while i < n:
    if a[i] >= days + 1:
        days += 1
        i += 1
    else:
        i += 1
print(days)

