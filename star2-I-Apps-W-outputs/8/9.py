
def solve(a, queries):
    n = len(a)
    m = len(queries)
    for i in range(m):
        l, r, x = queries[i]
        for j in range(l - 1, r):
            if a[j] != x:
                print(j + 1)
                break
        else:
            print(-1)


n, m = map(int, input().split())
a = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(m)]
solve(a, queries)

