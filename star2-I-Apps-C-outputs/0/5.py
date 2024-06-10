
from sys import stdin

def solve(n, k, graph, disqualified):
    return 0

def main():
    n, k = map(int, stdin.readline().split())
    graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
    disqualified = set(map(int, stdin.readline().split()))
    print(solve(n, k, graph, disqualified))

if __name__ == '__main__':
    main()

