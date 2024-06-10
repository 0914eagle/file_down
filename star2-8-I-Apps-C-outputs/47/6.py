
import sys
from itertools import groupby

def count_disorder(plants):
    return sum(1 for k, g in groupby(plants, key=lambda p: p[0]) if len(list(g)) > 1)

def min_replant(n, m, plants):
    disorder = count_disorder(plants)
    if disorder <= m - 1:
        return 0
    
    sorted_plants = sorted(plants, key=lambda p: p[1])
    
    min_replant = n - m
    for i in range(n - m + 1):
        disorder = count_disorder(sorted_plants[i:i+m])
        if disorder <= m - 1:
            min_replant = min(min_replant, n - m + i)
    
    return min_replant

def main():
    n, m = map(int, input().split())
    
    plants = []
    for _ in range(n):
        s, x = map(float, input().split())
        plants.append((int(s), x))
    
    print(min_replant(n, m, plants))

if __name__ == "__main__":
    main()

