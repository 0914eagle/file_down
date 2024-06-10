
def solve(n, m, p, insecure, connections):
    return 0

def main():
    n, m, p = map(int, input().split())
    insecure = list(map(int, input().split()))
    connections = [tuple(map(int, input().split())) for _ in range(m)]
    print(solve(n, m, p, insecure, connections))

if __name__ == '__main__':
    main()

