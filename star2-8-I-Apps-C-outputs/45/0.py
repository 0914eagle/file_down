
from math import gcd
n = int(input())
s = list(map(int, input().split()))

def can_take(s):
    for i in range(len(s)-1):
        if gcd(s[i], s[i+1]) != 1:
            return False
    
    return True

def take_pokemon(s):
    taken = 0
    for i in range(len(s)-1):
        if gcd(s[i], s[i+1]) == 1:
            taken += 1
    
    return taken+1

if can_take(s):
    print(take_pokemon(s))
else:
    s.sort(reverse=True)
    max_pokemon = 1
    for i in range(len(s)-1):
        if gcd(s[i], s[i+1]) != 1:
            continue
        
        max_pokemon += 1
    
    print(max_pokemon)

