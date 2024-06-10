
def solve(n, m, edges):
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)
    for u, v in edges:
        in_degree[v] += 1
        out_degree[u] += 1
    
    degree_diff = [in_degree[i] - out_degree[i] for i in range(1, n + 1)]
    degree_diff.sort(key=abs)
    
    edges.sort(key=lambda x: abs(in_degree[x[0]] - out_degree[x[0]]) + abs(in_degree[x[1]] - out_degree[x[1]]))
    
    for u, v in edges:
        if in_degree[u] > out_degree[u]:
            print(u, v)
        else:
            print(v, u)
    
    return sum([abs(d) for d in degree_diff]) // 2
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        edges = [list(map(int, input().split())) for _ in range(m)]
        print(solve(n, m, edges))

