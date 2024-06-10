
from itertools import permutations

def solve(n, m, d, your_minions, opponent_minions):
    total_minions = n + m
    all_permutations = permutations(range(total_minions))
    num_permutations = 0
    num_successful_permutations = 0
    for permutation in all_permutations:
        num_permutations += 1
        remaining_minions = [your_minions[i] for i in range(n) if permutation[i] < n] + [opponent_minions[i] for i in range(n, total_minions) if permutation[i] >= n]
        for _ in range(d):
            if len(remaining_minions) == 0:
                break
            remaining_minions[0] -= 1
            if remaining_minions[0] == 0:
                remaining_minions = remaining_minions[1:]
        if len(remaining_minions) == 0:
            num_successful_permutations += 1
    return num_successful_permutations / num_permutations

n, m, d = map(int, input().split())
your_minions = list(map(int, input().split()))
opponent_minions = list(map(int, input().split()))
print(solve(n, m, d, your_minions, opponent_minions))

