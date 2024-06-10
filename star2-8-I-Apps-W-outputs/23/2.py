

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def beehive_colony(n, m, paths):
    parent = [i for i in range(n)]
    
    for u, v in paths:
        union_parent(parent, u, v)
    
    for i in range(n):
        find_parent(parent, i)
    
    return len(set(parent))


n, m = map(int, input().split())
paths = [tuple(map(int, input().split())) for _ in range(m)]

res = beehive_colony(n, m, paths)

if res < 2:
    print("impossible")
else:
    print(res)


