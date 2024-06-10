
n, c = map(int, input().split())
w = list(map(int, input().split()))

sum = 0
count = 0
for i in w:
    if sum + i <= c:
        sum += i
        count += 1
print(count)

