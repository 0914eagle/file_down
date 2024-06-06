
# 1. 先找出最大值
# 2. 最大值与最大值的下一个元素交换
# 3. 重复1、2步

n = int(input())
a = list(map(int, input().split()))

ans = []
for i in range(n-1):
    m = max(a)
    idx = a.index(m)
    if idx == n-1:
        break
    ans.append(idx+1)
    a[idx], a[idx+1] = a[idx+1], a[idx]

if a == sorted(a):
    print(len(ans))
    for i in ans:
        print(i)
else:
    print(-1)
