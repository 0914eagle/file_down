
from sys import stdin
from itertools import combinations

def main():
    n, m = map(int, stdin.readline().split())
    p = list(map(int, stdin.readline().split()))
    foe_pairs = [tuple(map(int, stdin.readline().split())) for _ in range(m)]
    foe_pairs_set = set(foe_pairs)
    intervals = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if not any((i, k) in foe_pairs_set or (k, j) in foe_pairs_set for k in range(i+1, j)):
                intervals += 1
    print(intervals)

if __name__ == '__main__':
    main()

