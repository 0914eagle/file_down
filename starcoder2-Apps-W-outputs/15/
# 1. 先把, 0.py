
# 1. 先把所有数字排序
# 2. 然后从小到大遍历，如果当前数字的个位为0，则可以和前面的数字组成一个和
# 3. 如果当前数字的个位不为0，则和后面的数字组成一个和
# 4. 最后输出和的个数和和的数字

k = int(input())
d = list(map(int, input().split()))
d.sort()

ans = []
for i in range(k):
    if d[i] % 10 == 0:
        ans.append(d[i])
    else:
        if i + 1 < k:
            ans.append(d[i + 1])

print(len(ans))
print(*ans)
