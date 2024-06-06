
#n为节点数
#先对每个节点与其他节点的x，y坐标排序，找到最大的x，y坐标作为对角线，剩下的节点就是外界节点
#将所有的点按对角线做投影，这样就变成了直角坐标系
#先计算出内部点，因为内部点肯定是对角线的中点，对角线长度除以2就是对角线中点到任意一条边的距离
#再计算外部节点，如果某一个外部点在对角线的中点上，则距离为0，否则计算距离
n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
x = sorted(l, key=lambda x: x[0])
y = sorted(l, key=lambda x: x[1])
dx = x[-1][0] - x[0][0]
dy = y[-1][1] - y[0][1]
bx = x[0][0] + dx / 2
by = y[0][1] + dy / 2

res = 0

for p in l:
    if p[0] <= bx and p[1] >= by:
        #在内部
        res += dx / 2
    elif p[0] > bx and p[1] >= by:
        #在右下角
        res += max(p[0] - bx, by - p[1])
    elif p[0] > bx and p[1] < by:
        #在右上角
        res += max(p[0] - bx, p[1] - by)
    elif p[0] <= bx and p[1] < by:
        #在左上角
        res += max(bx - p[0], p[1] - by)
print(res/n)

