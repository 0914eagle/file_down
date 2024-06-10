
def solve(n, points):
    points.sort()
    path = ""
    x, y = 0, 0
    for point in points:
        dx, dy = point[0] - x, point[1] - y
        path += "R" * dx + "U" * dy
        x, y = point
    return path


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x, y))
        path = solve(n, points)
        if path:
            print("YES")
            print(path)
        else:
            print("NO")

