
from itertools import permutations

def solve(n, m, d, your_minions, opponent_minions):
    total_minions = n + m
    minions = your_minions + opponent_minions
    minions.sort(reverse=True)
    minions = [(minion, i < n) for i, minion in enumerate(minions)]
    probability = 0
    for permutation in permutations(minions):
        damage = d
        remaining_minions = total_minions
        for minion, is_your_minion in permutation:
            if minion > damage:
                minion -= damage
                damage = 0
            else:
                damage -= minion
                minion = 0
            if minion == 0:
                remaining_minions -= 1
            if damage == 0:
                break
        if remaining_minions == m:
            probability += 1
    probability /= factorial(total_minions)
    return probability

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n, m, d = map(int, input().split())
your_minions = list(map(int, input().split()))
opponent_minions = list(map(int, input().split()))
probability = solve(n, m, d, your_minions, opponent_minions)
print(probability)

