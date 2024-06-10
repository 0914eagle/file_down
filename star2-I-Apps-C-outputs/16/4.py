
from itertools import permutations

def prob_all_dead(n, m, d, your_minions, opponent_minions):
    total_minions = n + m
    total_damage = d
    minions_health = your_minions + opponent_minions
    minions_health.sort(reverse=True)
    minions_permutations = permutations(minions_health)
    total_ways = 0
    ways_all_dead = 0
    for permutation in minions_permutations:
        total_ways += 1
        damage_dealt = 0
        minions_remaining = total_minions
        for health in permutation:
            if health <= 0:
                continue
            if damage_dealt >= health:
                minions_remaining -= 1
                continue
            health -= 1
            damage_dealt += 1
            if health == 0:
                minions_remaining -= 1
        if minions_remaining <= m:
            ways_all_dead += 1
    return ways_all_dead / total_ways

n, m, d = map(int, input().split())
your_minions = list(map(int, input().split()))
opponent_minions = list(map(int, input().split()))
print(prob_all_dead(n, m, d, your_minions, opponent_minions))

