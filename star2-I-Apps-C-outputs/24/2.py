
def solve(n, edges):
    graph = [[0] * n for _ in range(n)]
    for u, v in edges:
        u, v = u - 1, v - 1
        graph[u][v] = graph[v][u] = 1
    chars = ['a', 'b', 'c']
    for c1 in chars:
        for c2 in chars:
            for c3 in chars:
                s = c1 + c2 + c3
                if is_valid(s, graph):
                    return 'Yes\n' + s
    return 'No'


def is_valid(s, graph):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] != (s[i] == s[j] or abs(ord(s[i]) - ord(s[j])) == 1):
                return False
    return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(solve(n, edges))

