
def process_query(n, p, u, k):
    adj_list = [[] for _ in range(n)]
    for i in range(1, n):
        adj_list[p[i-2]-1].append(i)

    result = []
    stack = [u-1]
    order = []
    while stack:
        curr = stack.pop()
        order.append(curr+1)
        stack.extend(adj_list[curr])

    if k <= len(order):
        result.append(order[k-1])
    else:
        result.append(-1)

    return result

n, q = map(int, input().split())
p = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]

for query in queries:
    result = process_query(n, p, query[0], query[1])
    print(result[0])
