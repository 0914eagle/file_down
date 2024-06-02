
def div_by_2(n):
    count = 0
    while n % 2 == 0:
        n = n // 2
        count += 1
    return count

N = int(input())

max_count = 0
ans = 0
for i in range(1, N+1):
    count = div_by_2(i)
    if count > max_count:
        max_count = count
        ans = i

print(ans)

