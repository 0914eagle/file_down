
n = int(input())
a = list(map(int, input().split()))

max_num = max(a)

l = 0
r = 0

for i in range(n):
    if a[i] == max_num:
        l = i
        break

for i in range(n - 1, -1, -1):
    if a[i] == max_num:
        r = i
        break

print(l + 1, r + 1)
