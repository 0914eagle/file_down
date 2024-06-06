
import sys
import collections

read = sys.stdin.readline

n, m = map(int, read().split())
ship = [tuple(map(int, read().split())) for _ in range(m)]
ship.sort()

# This function will check the direction of torpedo in each step
# and returns the number of ships that will be hit
def check(direction):
    visited = set()
    cnt = 0
    x, y = 0, 0
    for _ in range(n):
        x += direction
        y += 1
        if (x, y) in visited:
            continue
        for a, b, c in ship:
            if a <= x <= b and y == c:
                cnt += 1
        visited.add((x, y))
    return cnt


# Checking if it is possible to go to the right and up
cnt = check(1)

# Checking if it is possible to stay still and up
if cnt == check(0):
    print("impossible")
    exit(0)

# Checking if it is possible to go to the left and up
if cnt == check(-1):
    print("impossible")
    exit(0)

# Finding the final direction for the torpedo in each step
res = []
x, y = 0, 0
for _ in range(n):
    x += 1
    y += 1
    for a, b, c in ship:
        if a <= x <= b and y == c:
            res.append("-")
            x -= 2
            break
    else:
        res.append("+")

print("".join(res))
