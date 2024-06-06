
n = int(input())
a = list(map(int, input().split()))

max_count = 0
max_num = 0
for i in range(n):
    count = 0
    for j in range(n):
        if a[i] == a[j]:
            count += 1
    if count > max_count:
        max_count = count
        max_num = a[i]

l = 0
r = 0
for i in range(n):
    if a[i] == max_num:
        l = i
        break
for i in range(n):
    if a[n-1-i] == max_num:
        r = n-1-i
        break

print(l+1, r+1)
