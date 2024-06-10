
n = int(input())
max_count = 0
max_num = 0
for i in range(1, n+1):
    count = 0
    num = i
    while num % 2 == 0:
        num //= 2
        count += 1
    if count > max_count:
        max_count = count
        max_num = i
print(max_num)

