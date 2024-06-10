
from random import random

def solve(N, payout, prob):
    def simulate(pos):
        if random() < prob[pos][4]:
            return payout[pos]
        else:
            neighbors = [i for i in range(len(prob[pos])) if prob[pos][i] > 0]
            next_pos = neighbors[int(random() * len(neighbors))]
            return simulate(next_pos)

    total_payout = 0
    for i in range(100000):
        total_payout += simulate(0)
    return total_payout / 100000

N = int(input())
payout = list(map(int, input().split()))
prob = [list(map(float, input().split())) for _ in range(N * (N+1) // 2)]
print(solve(N, payout, prob))

