
# 这道题的算法可以分为以下几步:
#   1. 首先, 所有数对的差值为 di, 其中 di = ai - aj
#   2. 若存在某个数对 a 和 b, 使得 a - b = c - d, 则有 a + d = b + c
#   3. 若存在某个数对 a 和 b, 使得 a + b = c + d, 则有 a - d = b - c
#   4. 因此, 我们可以从已经得到的差值集合中找到一些满足条件的数对, 将其中的数相加
#   5. 考虑到如果存在某个数 a, 满足 a + a = 2 * a = 0, 因此我们首先需要将 0 移除出差值集合
#   6. 最后, 将得到的所有满足条件的数对中的数相加, 得到的和即为答案

n = int(input())
M = []
for i in range(n):
    M.append(list(map(int, input().split())))

# 计算差值
nums = set()
for i in range(n):
    for j in range(n):
        if i != j:
            nums.add(M[i][j] - M[j][i])

# 移除 0
nums.remove(0)

# 寻找满足条件的数对
pairs = []
for num in nums:
    if -num in nums:
        pairs.append([num, -num])

# 计算答案
ans = 0
for pair in pairs:
    ans += pair[0]

print(ans)
