
import sys


class Tree:
    def __init__(self, n):
        self.adj_list = [[] for _ in range(n)]
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)


def dfs(u, p, colors):
    red = 0
    blue = 0
    for v in tree.adj_list[u]:
        if v == p:
            continue
        
        red_v, blue_v = dfs(v, u, colors)
        red += red_v
        blue += blue_v
    
    if colors[u] == 1:
        red += 1
    elif colors[u] == 2:
        blue += 1
    
    return red, blue


def solve(tree, colors):
    red, blue = dfs(0, -1, colors)
    
    if red > 0 and blue > 0:
        return 1
    
    return 0


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    colors = list(map(int, input().split()))
    tree = Tree(n)
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        tree.add_edge(u, v)
    
    print(solve(tree, colors))

