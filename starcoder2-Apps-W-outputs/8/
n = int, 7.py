
n = int(input())
a = list(map(int, input().split()))

max_num = max(a)
max_num_index = []
for i in range(n):
    if a[i] == max_num:
        max_num_index.append(i)

max_num_index.append(n)

ans = []
for i in range(len(max_num_index) - 1):
    ans.append(max_num_index[i + 1] - max_num_index[i])

print(max_num_index[ans.index(min(ans))], max_num_index[ans.index(min(ans)) + 1])
