
n, l = map(int, input().split())

sum_all = 0
for i in range(n):
    sum_all += l + i - 1

diff_min = float('inf')
for i in range(n):
    diff = abs(sum_all - (l + i - 1))
    if diff < diff_min:
        diff_min = diff

print(sum_all - diff_min)

