
def solve(n, m, teleports):
    pass

if __name__ == '__main__':
    n, m = map(int, input().split())
    teleports = []
    for _ in range(n):
        a, b = map(int, input().split())
        teleports.append((a, b))
    
    print(solve(n, m, teleports))

