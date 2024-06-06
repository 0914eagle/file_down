
# 这题题意就很晕 就是说n个图标，m个图标不动，删除剩下的n个，要删除的图标不得移动
# 要移动的图标，要把要删除的图标尽量移动到一起，然后一个删除命令就可以搞定。
# 思路：所有要删除的图标和不动的图标都放到一个列表中，从左到右排序，
# 每次都找一下他们之间的最短距离（删去最多图标的最短距离），
# 然后每次都把要删除的图标中的最左边的图标和图标移动到距离最小的位置上

import sys

for line in sys.stdin:
    line = line.strip()
    if line == "":
        continue
    n, m = list(map(int, line.split()))
    # print(n,m)
    x = []
    for i in range(2*n):
        x.append(list(map(int, sys.stdin.readline().strip().split())))
    x.sort(key=lambda a: a[1])
    if m == 0:
        print(n)
    else:
        # print(x)
        result = 0
        # print(x)
        while n > 0:
            min_distance = 10000000
            index = 0
            for i in range(n):
                for j in range(m):
                    temp = abs(x[i][1]-x[n+j][1])+15
                    if temp < min_distance:
                        min_distance = temp
                        index = i
            # print(index)
            result += min_distance
            x[index][1] = x[n+m-1][1]
            x[n+m-1][1] = x[index][1]+9
            x.sort(key=lambda a: a[1])
            n -= 1
            m -= 1
        print(result)
