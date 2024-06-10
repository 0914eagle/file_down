
n = int(input())
arr = [int(x) for x in input().split()]
pos = {}
for i, x in enumerate(arr):
    pos[x] = i
sorted_arr = sorted(arr)
cnt = 0
for i, x in enumerate(sorted_arr):
    if pos[x] != i:
        cnt += 1
print(cnt)

