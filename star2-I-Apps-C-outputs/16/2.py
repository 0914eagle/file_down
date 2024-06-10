
from itertools import product

def solve(n, m, d, your_minions, opponent_minions):
    your_minions = sorted(your_minions)
    opponent_minions = sorted(opponent_minions)
    total_minions = n + m
    minions_left = total_minions
    damage_left = d
    probability = 1
    for i in range(n):
        probability *= your_minions[i] / total_minions
    for i in range(m):
        probability *= opponent_minions[i] / total_minions
    for i in range(n):
        for j in range(m):
            probability *= (total_minions - minions_left) / total_minions
            if your_minions[i] > opponent_minions[j]:
                probability *= opponent_minions[j] / your_minions[i]
            else:
                probability *= your_minions[i] / opponent_minions[j]
            minions_left -= 1
            damage_left -= 1
            if damage_left == 0:
                break
        if damage_left == 0:
            break

    return probability

n, m, d = map(int, input().split())
your_minions = list(map(int, input().split()))
opponent_minions = list(map(int, input().split()))

probability = solve(n, m, d, your_minions, opponent_minions)
print(probability)

