
def solve(n, m, k, ore, coal, adj_list):
    return 0
n, m, k = map(int, input().split())
ore = list(map(int, input().split()))
coal = list(map(int, input().split()))
adj_list = [[] for _ in range(n)]
for i in range(n):
    a, *bs = map(int, input().split())
    adj_list[i] = bs
print(solve(n, m, k, ore, coal, adj_list))

