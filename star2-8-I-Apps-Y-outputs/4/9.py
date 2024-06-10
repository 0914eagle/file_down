
n = int(input())
a = [int(i) for i in input().split()]

a = sorted(a, reverse=True)

total_sum = sum(a)

snuke_sum = 0
for i in range(len(a)):
    snuke_sum += a[i]
    total_sum -= a[i]
    if snuke_sum > total_sum:
        break

print(abs(snuke_sum - total_sum))

