
from itertools import combinations

def solve(n, m, d, your_minions, opponent_minions):
    total_minions = n + m
    total_damage = d * total_minions
    minion_health = your_minions + opponent_minions
    
    minions_to_damage = combinations(range(total_minions), total_damage)
    
    total_ways = 0
    ways_to_remove_opponent = 0
    
    for minions in minions_to_damage:
        total_ways += 1
        
        minions_remaining = [minion_health[i] for i in range(total_minions) if i not in minions]
        
        if sum(minions_remaining) <= 0:
            ways_to_remove_opponent += 1
            
    return ways_to_remove_opponent / total_ways
    
n, m, d = map(int, input().split())
your_minions = list(map(int, input().split()))
opponent_minions = list(map(int, input().split()))

print(solve(n, m, d, your_minions, opponent_minions))

