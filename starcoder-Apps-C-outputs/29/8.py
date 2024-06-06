
# 解题思路
# 对于每个点，假设该点为起点，则对每个点，先判断该点与其他点的连线中是否有边界线，如果有则该条边不可以作为路线
# 如果没有，则假设该点为终点，则起点到终点的距离为该点到所有边界线的距离总和减去2
# 最终对所有点的距离求和即为结果

def main():
    n = int(input())
    points = []
    for _ in range(n):
        points.append(list(map(int, input().split())))
    res = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            if i != j:
                x = points[i][0]
                y = points[i][1]
                x1 = points[j][0]
                y1 = points[j][1]
                if x == x1:
                    if y < y1:
                        if not has_line(x, y, x, y1, points):
                            tmp += (y1-y)
                    else:
                        if not has_line(x, y1, x, y, points):
                            tmp += (y-y1)
                elif y == y1:
                    if x < x1:
                        if not has_line(x, y, x1, y, points):
                            tmp += (x1-x)
                    else:
                        if not has_line(x1, y, x, y, points):
                            tmp += (x-x1)
        res += tmp
    print(res/(n*n))

def has_line(x, y, x1, y1, points):
    for point in points:
        x2 = point[0]
        y2 = point[1]
        if x == x2 or y == y2:
            if (x == x2 and y2 >= min(y, y1) and y2 <= max(y, y1)) or (y == y2 and x2 >= min(x, x1) and x2 <= max(x, x1)):
                return True
    return False

if __name__ == '__main__':
    main()
