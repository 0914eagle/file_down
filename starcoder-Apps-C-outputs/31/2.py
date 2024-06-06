
'''
输入：
2 0.5
2 0.5
1 0.5

输出：
1
'''
# N:箱子数量
# P:需要的概率
N,P=map(float,input().split())
sum=0
count=0
for i in range(int(N)):
    # e:能量
    # p:概率
    e,p=map(float,input().split())
    sum+=e*p

# 计算出需要达到的值
p1=sum*N
# 然后对p进行排序，选择最小的能量值
p2=p1/P
print(p2)

# 理解题目：最小的能量消耗
# 1、计算出能量消耗的平均值
# 2、概率最小的能量消耗需要的最小值
