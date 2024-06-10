
import sys

def catch_fish(lake, r, c, k, l):
    fish_points = [(x, y) for x in range(r) for y in range(c) if lake[x][y] <= l and lake[x][y] + k >= 1]
    can_catch = [(x, y) for (x, y) in fish_points if (x, y) == (0, 0) or (x - 1, y) in fish_points or (x, y - 1) in fish_points or (x + 1, y) in fish_points or (x, y + 1) in fish_points]
    
    return len(can_catch)


def main():
    r, c, k, l = map(int, sys.stdin.readline().split())
    x0, y0 = map(int, sys.stdin.readline().split())
    lake = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
    
    print(catch_fish(lake, r, c, k, l))


if __name__ == '__main__':
    main()


