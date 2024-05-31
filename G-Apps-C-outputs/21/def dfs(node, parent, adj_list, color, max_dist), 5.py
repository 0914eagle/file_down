
MOD = 10**9 + 7

def dfs(node, parent, adj_list, color, max_dist):
    max_dist[node][color] = 0
    for child in adj_list[node]:
        if child != parent:
            dfs(child, node, adj_list, color, max_dist)
            max_dist[node][color] = max(max_dist[node][color], max_dist[child][color] + 1)

def solve_tree_painting():
    N = int(input())
    adj_list = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        adj_list[a - 1].append(b - 1)
        adj_list[b - 1].append(a - 1)

    max_dist = [[0, 0] for _ in range(N)]
    dfs(0, -1, adj_list, 0, max_dist)
    dfs(0, -1, adj_list, 1, max_dist)

    total_niceness = 0
    for node in range(N):
        total_niceness += max(max_dist[node][0], max_dist[node][1])
        total_niceness %= MOD

    print(total_niceness)

solve_tree_painting()
