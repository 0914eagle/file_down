
import sys
from collections import deque

def solve(f, s, g, u, d):
    def bfs(s, g, u, d):
        q = deque([(s, 0)])
        visited = set()
        while q:
            curr, pushes = q.popleft()
            if curr == g:
                return pushes
            if curr > g:
                continue
            if curr not in visited:
                visited.add(curr)
                q.append((curr + u, pushes + 1))
                q.append((curr - d, pushes + 1))
        return -1

    res = bfs(s, g, u, d)
    if res != -1:
        return str(res)
    else:
        return "use the stairs"

def main():
    f, s, g, u, d = map(int, input().split())
    print(solve(f, s, g, u, d))

if __name__ == "__main__":
    main()

