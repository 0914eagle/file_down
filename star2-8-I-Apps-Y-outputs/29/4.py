
n = int(input())
a = [int(x) for x in input().split()]
a.sort()

day = 0
count = 0
for i in a:
    day += 1
    if i >= day:
        count += 1
    else:
        break
print(count)

