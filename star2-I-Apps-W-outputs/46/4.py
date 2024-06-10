
def solve(n, m, groups):
    return "YES" if n == 1 else "NO"

if __name__ == "__main__":
    n, m = map(int, input().split())
    groups = []
    for _ in range(m):
        group = list(map(int, input().split()))
        groups.append(group)
    
    print(solve(n, m, groups))

