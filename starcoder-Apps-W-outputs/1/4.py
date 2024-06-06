
# 题目大意
# 给定n个点和m条线段，问是否存在一个数k使得k度旋转对称
# 输出：Yes or No
# 思路：
# 遍历n个点，找到一个与其他点对称的点，即可

n, m = map(int, input().split())
d = {}
for i in range(n):
    d[i + 1] = 0
for _ in range(m):
    a, b = map(int, input().split())
    d[a] += 1
    d[b] += 1
count = 0
for k, v in d.items():
    if v == 2:
        count += 1
if count == n:
    print('Yes')
else:
    print('No')
