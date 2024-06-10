
t = int(input())
for _ in range(t):
    n = int(input())
    unfairness = 0
    last = 0
    current = 1
    while current <= n:
        unfairness += (current ^ last).bit_count()
        last = current
        current <<= 1
    print(unfairness)

