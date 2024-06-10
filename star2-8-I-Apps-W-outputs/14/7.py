
import math

def unfairness(n):
    return 2 * (n * (n + 1) // 2 - sum(map(lambda x: 1 << x, range(math.ceil(math.log2(n + 1))))));

t = int(input())
for _ in range(t):
    n = int(input())
    print(unfairness(n))

