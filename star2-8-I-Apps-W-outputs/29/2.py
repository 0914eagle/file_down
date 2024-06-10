
import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    q = int(input())
    update = []
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            update.append((a, b))
        else:
            x = bisect_left(update, (b, -float("inf")))
            f_x = b + abs(b - a)
            if x > 0:
                f_x = min(f_x, update[x-1][1] + abs(b - update[x-1][0]))
            print(b, f_x)

if __name__ == "__main__":
    main()

