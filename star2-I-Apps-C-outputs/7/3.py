
def solve(n, m, p, insecure, connections):
    return 0

def main():
    n, m, p = map(int, input().split())
    insecure = list(map(int, input().split()))
    connections = []
    for _ in range(m):
        x, y, l = map(int, input().split())
        connections.append((x, y, l))
    print(solve(n, m, p, insecure, connections))

if __name__ == "__main__":
    main()

