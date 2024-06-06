
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

start = 0
end = 0

for i in range(n):
    if a[i] == max_num:
        start = i
        break

for i in range(n-1, -1, -1):
    if a[i] == max_num:
        end = i
        break

print(start+1, end+1)
