
import sys

def solve(n, packages):
    packages = sorted(packages, key=lambda p: (p[0], p[1]))
    curr_x, curr_y = 0, 0
    path = ""
    for x, y in packages:
        if curr_x < x:
            path += "R" * (x - curr_x)
            curr_x = x
        if curr_y < y:
            path += "U" * (y - curr_y)
            curr_y = y
    return path

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        packages = []
        for _ in range(n):
            x, y = map(int, input().split())
            packages.append((x, y))
        path = solve(n, packages)
        if path:
            print("YES")
            print(path)
        else:
            print("NO")

if __name__ == "__main__":
    main()

