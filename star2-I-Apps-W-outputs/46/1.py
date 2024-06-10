
def solve(n, m, groups):
    pass

if __name__ == '__main__':
    n, m = map(int, input().split())
    groups = []
    for _ in range(m):
        k, *group = map(int, input().split())
        groups.append(group)
    
    print(solve(n, m, groups))

