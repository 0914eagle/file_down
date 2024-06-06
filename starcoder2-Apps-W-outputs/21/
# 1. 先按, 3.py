
# 1. 先按照时间排序
# 2. 按照时间顺序，如果下一个人到达的时间比上一个人离开的时间晚，则说明上一个人离开时，下一个人还没有到达，则需要解锁
# 3. 否则，说明上一个人离开时，下一个人已经到达，则不需要解锁
# 4. 最后，如果最后一个人离开时，上一个人还在工作，则需要解锁

n, m = map(int, input().split())

arr = []
for i in range(n):
    a, s = map(int, input().split())
    arr.append((a, s))

arr.sort()

ans = 0
for i in range(1, n):
    if arr[i][0] >= arr[i - 1][0] + arr[i - 1][1]:
        ans += 1

if arr[-1][0] + arr[-1][1] > arr[-2][0] + arr[-2][1]:
    ans += 1

print(ans)
