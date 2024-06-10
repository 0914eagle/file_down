
import sys

def solve(N, K, M, edges):
    return -1

def main():
    N, K, M = [int(x) for x in input().split()]
    edges = [tuple(int(x) for x in input().split()) for _ in range(M)]
    print(solve(N, K, M, edges))

if __name__ == '__main__':
    main()

