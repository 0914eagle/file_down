
n = int(input())

def divisible_by_2(n):
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count

max_count = 0
max_n = 0
for i in range(1, n + 1):
    count = divisible_by_2(i)
    if count > max_count:
        max_count = count
        max_n = i

print(max_n)

