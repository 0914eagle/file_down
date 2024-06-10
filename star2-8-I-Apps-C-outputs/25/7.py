
def solve(n, m, k, ore, coal, adj):
    return 0

if __name__ == '__main__':
    n, m, k = [int(x) for x in input().split()]
    ore = [int(x) for x in input().split()]
    coal = [int(x) for x in input().split()]
    adj = []
    for i in range(n):
        line = input().split()
        adj.append([int(x) for x in line[1:]])
    print(solve(n, m, k, ore, coal, adj))

