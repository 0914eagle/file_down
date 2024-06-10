
def solve(a, queries):
    n = len(a)
    m = len(queries)
    for i in range(m):
        l, r, x = queries[i]
        for j in range(l, r+1):
            if a[j-1] != x:
                print(j)
                break
        else:
            print(-1)

n, m = map(int, input().split())
a = list(map(int, input().split()))
queries = []
for i in range(m):
    l, r, x = map(int, input().split())
    queries.append((l, r, x))
solve(a, queries)

