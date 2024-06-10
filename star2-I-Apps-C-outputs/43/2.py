
from math import factorial
from random import random

def nCk(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def solve(n, payouts, probs):
    def simulate(hole):
        if hole == 1:
            return payouts[0]
        else:
            r = random()
            if r < probs[hole - 1][0]:
                return simulate(hole - n)
            elif r < probs[hole - 1][0] + probs[hole - 1][1]:
                return simulate(hole - n + 1)
            elif r < probs[hole - 1][0] + probs[hole - 1][1] + probs[hole - 1][2]:
                return simulate(hole + n - 1)
            elif r < probs[hole - 1][0] + probs[hole - 1][1] + probs[hole - 1][2] + probs[hole - 1][3]:
                return simulate(hole + n)
            else:
                return payouts[hole - 1]

    total = 0
    for _ in range(1000000):
        total += simulate(n * (n + 1) // 2)
    return total / 1000000

n = int(input())
payouts = list(map(int, input().split()))
probs = [list(map(float, input().split())) for _ in range(n * (n + 1) // 2)]
print(solve(n, payouts, probs))

