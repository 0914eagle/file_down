
import itertools
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

indices = list(range(0, n))
indices_groups = list(itertools.combinations(indices, k-1))
ans = 0
ans_list = []
for index_group in indices_groups:
    s = 0
    for i in range(k):
        if i == 0:
            tmp_nums = nums[0:index_group[i] + 1]
        elif i == k - 1:
            tmp_nums = nums[index_group[i-1] + 1:]
        else:
            tmp_nums = nums[index_group[i-1] + 1:index_group[i] + 1]
        s += sum(sorted(tmp_nums)[len(tmp_nums) - m:])
    if s > ans:
        ans = s
        ans_list = index_group
print(ans)
print(" ".join(map(lambda x: str(x+1), ans_list)))
