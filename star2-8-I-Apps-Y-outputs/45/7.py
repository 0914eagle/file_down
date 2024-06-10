
def solve(n, a, adj_list):
    return 0


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    adj_list = [[] for _ in range(n)]
    for _ in range(n - 1):
        v, u = map(int, input().split())
        v, u = v - 1, u - 1
        adj_list[v].append(u)
        adj_list[u].append(v)
    print(solve(n, a, adj_list))

