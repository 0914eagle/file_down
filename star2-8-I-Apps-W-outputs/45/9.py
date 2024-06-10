
import sys

def find_max_cities(n, m, roads):
    adj_list = [[] for _ in range(n)]
    for u, v in roads:
        adj_list[u-1].append(v-1)
    
    in_degree = [0] * n
    out_degree = [0] * n
    
    for u in range(n):
        for v in adj_list[u]:
            out_degree[u] += 1
            in_degree[v] += 1
    
    max_cities = 0
    
    for u in range(n):
        if out_degree[u] == in_degree[u]:
            max_cities += 1
    
    return max_cities

def find_oriented_roads(n, m, roads):
    adj_list = [[] for _ in range(n)]
    for u, v in roads:
        adj_list[u-1].append(v-1)
    
    in_degree = [0] * n
    out_degree = [0] * n
    
    for u in range(n):
        for v in adj_list[u]:
            out_degree[u] += 1
            in_degree[v] += 1
    
    for u in range(n):
        for v in adj_list[u]:
            if out_degree[u] > in_degree[u]:
                yield u+1, v+1

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        roads = []
        
        for _ in range(m):
            u, v = map(int, sys.stdin.readline().split())
            roads.append((u, v))
        
        max_cities = find_max_cities(n, m, roads)
        print(max_cities)
        
        for u, v in find_oriented_roads(n, m, roads):
            print(u, v)

