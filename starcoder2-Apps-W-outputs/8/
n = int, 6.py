
n = int(input())
a = list(map(int, input().split()))

l = 0
r = 0
max_num = 0
max_count = 0

for i in range(n):
    if a[i] == max_num:
        max_count += 1
    elif a[i] > max_num:
        max_num = a[i]
        max_count = 1
    if max_count > r - l + 1:
        l = i - max_count + 2
        r = i
print(l + 1, r + 1)
