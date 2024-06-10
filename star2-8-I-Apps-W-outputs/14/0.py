
from math import ceil, log

def unfairness(n):
    unf = 0
    for i in range(n + 1):
        unf += log(i + 1, 2)
    return ceil(unf)

t = int(input())
for i in range(t):
    n = int(input())
    print(unfairness(n))

