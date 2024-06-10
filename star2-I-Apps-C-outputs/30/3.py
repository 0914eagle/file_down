
from functools import reduce
from operator import pow

MODULO = 10**9 + 7

def n_choose_k(n, k):
    if k < 0 or n < k:
        return 0
    return reduce(lambda x, y: x * y, range(n - k + 1, n + 1)) // reduce(lambda x, y: x * y, range(1, k + 1))

def solve(a, b):
    return n_choose_k(a + b, a)

def main():
    n = int(input())
    ways = 1
    for _ in range(n):
        a, b = map(int, input().split())
        ways = (ways * solve(a, b)) % MODULO
    print(ways)

if __name__ == '__main__':
    main()

