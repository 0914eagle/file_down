
import sys

def solve(x, y):
    path = ""
    while x > 0:
        path += "R"
        x -= 1
    while y > 0:
        path += "U"
        y -= 1
    return path

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        packages = []
        for _ in range(n):
            x, y = map(int, input().split())
            packages.append((x, y))
        packages.sort()
        path = ""
        for x, y in packages:
            path += solve(x, y)
        print("YES")
        print(path)

if __name__ == "__main__":
    main()

