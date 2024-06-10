
import sys
from itertools import product

def is_valid(n, m, k, x, y, obstacles, path):
    if x < 0 or x >= n or y < 0 or y >= m or (x, y) in obstacles:
        return False
    if path and (x, y) == path[0]:
        return len(path) == k
    return True

def find_path(n, m, k, x, y, obstacles):
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    queue = [(x, y, "")]
    visited = set()
    while queue:
        x, y, path = queue.pop(0)
        if len(path) >= k:
            continue
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(n, m, k, nx, ny, obstacles, path):
                queue.append((nx, ny, path + "LDRU"[moves.index((dx, dy))]))
    
    if not queue:
        return "IMPOSSIBLE"
    queue.sort()
    return queue[0][2]

def main():
    n, m, k = map(int, input().split())
    obstacles = set()
    x, y = None, None
    for i in range(n):
        line = input()
        for j, c in enumerate(line):
            if c == "*":
                obstacles.add((i, j))
            elif c == "X":
                x, y = i, j
    print(find_path(n, m, k, x, y, obstacles))

if __name__ == "__main__":
    main()

