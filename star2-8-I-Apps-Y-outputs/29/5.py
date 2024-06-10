
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
count = 0
days = 0
for i in a:
    count += i
    days += 1
    if count >= days:
        continue
    else:
        break
print(days)

