
from sys import stdin

def solve(n, a, b):
    return 1

def main():
    n = int(stdin.readline())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, stdin.readline().split())
    print(solve(n, a, b))

main()

