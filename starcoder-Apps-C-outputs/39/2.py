
#先将所有的加油站按照位置从小到大排序，然后依次检查能否到达
#如果可以到达，则计算到达这个加油站的花费，然后将当前位置前移，将当前剩余的油加上这个加油站加的油
#否则，将当前位置前移，并将当前剩余油量减去这一段距离的油量
#如果剩余的油量小于0，则将当前剩余油量设为0
n, g = map(int, input().split())
station = []
for i in range(n):
    d, c = map(int, input().split())
    station.append([d, c])

station.sort()

pre = 0
pre_oil = g
cost = 0

for i in range(n):
    if pre_oil >= station[i][0] - pre:
        cost += (station[i][0] - pre) * station[i][1]
        pre_oil -= (station[i][0] - pre)
        pre_oil += station[i][1]
        pre = station[i][0]
    else:
        pre = station[i][0]
        pre_oil -= (station[i][0] - pre)
        if pre_oil < 0:
            pre_oil = 0

if pre_oil > 0:
    print(cost)
else:
    print("cancel road trip")
