
from itertools import combinations

def prob_all_dead(your_health, opponent_health, damage):
    your_health = sorted(your_health)
    opponent_health = sorted(opponent_health)
    total_minions = len(your_health) + len(opponent_health)
    total_damage = damage * total_minions
    total_health = sum(your_health) + sum(opponent_health)
    if total_damage >= total_health:
        return 1.0
    minions_killed = 0
    for i in range(len(your_health)):
        if your_health[i] <= damage:
            minions_killed += 1
        else:
            break
    for i in range(len(opponent_health)):
        if opponent_health[i] <= damage:
            minions_killed += 1
        else:
            break
    prob = 1.0
    for i in range(minions_killed, total_minions + 1):
        prob *= (total_minions - i) / (total_minions - i + 1)
    return prob

n, m, d = map(int, input().split())
your_health = list(map(int, input().split()))
opponent_health = list(map(int, input().split()))
print(prob_all_dead(your_health, opponent_health, d))

