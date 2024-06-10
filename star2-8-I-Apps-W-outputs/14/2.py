

from math import log2, ceil

def unfairness(n: int) -> int:
    bin_n = bin(n)[2:]
    unfairness = 0
    for i in range(len(bin_n) - 1):
        unfairness += (1 << (len(bin_n) - i - 1))
    return unfairness

t = int(input())
for _ in range(t):
    n = int(input())
    print(unfairness(n))


