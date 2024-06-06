
# 1. 先把所有可能的组合列出来
# 2. 然后对每一个组合进行判断
# 3. 最后输出

from itertools import product

def check(a, b, c):
    a, b, c = str(a), str(b), str(c)
    if len(set(a + b + c)) == len(a) + len(b) + len(c):
        return True
    return False

def solve(n):
    ans = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if check(i, j, i + j):
                ans.append((i, j))
    return ans

n = int(input())
ans = solve(n)
print(len(ans))
for i, j in ans:
    print(i, j)
