
import sys

def switches(N, M, k, s, p):
    # Write your code here
    return 0

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    k = [int(x) for x in sys.stdin.readline().split()]
    s = [[int(x) for x in sys.stdin.readline().split()] for _ in range(M)]
    p = [int(x) for x in sys.stdin.readline().split()]
    print(switches(N, M, k, s, p))

