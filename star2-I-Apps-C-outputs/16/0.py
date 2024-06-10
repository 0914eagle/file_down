
from itertools import product

def solve(n, m, d, your_minions, opponent_minions):
    def get_probability(your_minions, opponent_minions):
        if not your_minions or not opponent_minions:
            return 0
        if d == 0:
            return 1
        probability = 0
        for damage_distribution in product(range(1, 7), repeat=d):
            remaining_your_minions = [health - damage for health, damage in zip(your_minions, damage_distribution)]
            remaining_opponent_minions = [health - damage for health, damage in zip(opponent_minions, damage_distribution)]
            probability += get_probability(remaining_your_minions, remaining_opponent_minions)
        return probability / 6 ** d

    return get_probability(your_minions, opponent_minions)

n, m, d = map(int, input().split())
your_minions = list(map(int, input().split()))
opponent_minions = list(map(int, input().split()))
print(solve(n, m, d, your_minions, opponent_minions))

