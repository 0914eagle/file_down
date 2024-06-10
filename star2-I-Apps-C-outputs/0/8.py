
import sys

def find_smallest_set(n, k, graph, disqualified):
    return 0

def main():
    n, k = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    disqualified = list(map(int, sys.stdin.readline().split()))
    print(find_smallest_set(n, k, graph, disqualified))

if __name__ == '__main__':
    main()

