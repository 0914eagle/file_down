
import sys

def solve(h, w, page):
    def dfs(x, y, i):
        if not (0 <= x < h and 0 <= y < w and (x, y) not in vis and page[x][y] in allowed):
            return
        vis.add((x, y))
        res[i] += 1
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            dfs(x + dx, y + dy, i)
    allowed = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?!,.")
    page = [list(row) for row in page]
    vis = set()
    res = []
    for i in range(len(page)):
        for j in range(len(page[0])):
            if page[i][j] in allowed:
                continue
            res.append(0)
            dfs(i, j, len(res) - 1)
    if not res:
        return page
    best = res.index(min(res))
    for i in range(len(page)):
        for j in range(len(page[0])):
            if (i, j) in vis and res[best] > 0:
                page[i][j] = " "
                res[best] -= 1
    return page

def main():
    h, w = map(int, input().split())
    page = []
    for _ in range(h):
        page.append(input())
    res = solve(h, w, page)
    if res is None:
        print("Invalid input")
        return
    for row in res:
        print("".join(row))

if __name__ == "__main__":
    main()

