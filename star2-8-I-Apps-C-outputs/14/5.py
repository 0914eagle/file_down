
def fishing_contest(r, c, k, l, x0, y0, t):
    def can_catch_fish(x, y, time):
        return t[x][y] <= time <= t[x][y] + k
    
    def dfs(x, y, time, visited):
        if (x, y) in visited:
            return 0
        if not can_catch_fish(x, y, time):
            return 0
        visited.add((x, y))
        
        res = 1
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                res += dfs(nx, ny, time + 1, visited)
        return res
    
    return dfs(x0, y0, 1, set())
    
r, c, k, l = map(int, input().split())
x0, y0 = map(int, input().split())
t = []
for _ in range(r):
    t.append(list(map(int, input().split())))
print(fishing_contest(r, c, k, l, x0, y0, t))

