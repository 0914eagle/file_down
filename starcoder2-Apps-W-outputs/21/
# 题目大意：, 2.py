
# 题目大意：给定一个长度为n的序列，每个数有两个属性，一个是到达时间，一个是停留时间，
# 问最多能有多少个数满足到达时间小于等于停留时间。
# 思路：先对到达时间排序，然后从第一个数开始，到达时间小于等于停留时间的数的个数就是答案。
# 注意：如果到达时间相同，停留时间越长的排在前面。

n,m=map(int,input().split())
a=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append([x,y])
a.sort(key=lambda x:x[0])
ans=0
for i in range(n):
    if a[i][0]<=a[i][1]:
        ans+=1
print(ans)
