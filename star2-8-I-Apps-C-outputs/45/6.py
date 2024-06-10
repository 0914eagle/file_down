
from itertools import combinations
from math import gcd

def max_pokemon(n, s):
    max_pokemon = 0
    for k in range(n, 0, -1):
        for combination in combinations(s, k):
            if gcd(*combination) == 1:
                max_pokemon = k
                break
        if max_pokemon:
            break
    
    return max_pokemon
n = int(input())
s = list(map(int, input().split()))
print(max_pokemon(n, s))

