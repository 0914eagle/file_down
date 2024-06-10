
import sys
from math import atan2, pi

def solve(opponents):
    angles = []
    for x, y, r in opponents:
        angle = atan2(y, x)
        angles.append((angle, r))
    angles.sort()
    max_hits = 0
    for i in range(len(angles)):
        hits = 1
        angle, r = angles[i]
        for j in range(i + 1, len(angles)):
            angle2, r2 = angles[j]
            if angle2 - angle > pi:
                break
            if abs(angle2 - angle) < r + r2:
                hits += 1
        max_hits = max(max_hits, hits)
    return max_hits

def main():
    n = int(sys.stdin.readline().strip())
    opponents = []
    for _ in range(n):
        x, y, r = map(float, sys.stdin.readline().strip().split())
        opponents.append((x, y, r))
    print(solve(opponents))

if __name__ == '__main__':
    main()

