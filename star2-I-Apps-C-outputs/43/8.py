
import random

def solve(N, payouts, probs):
    def simulate():
        curr = 0
        while True:
            if random.random() < probs[curr][4]:
                return payouts[curr]
            curr += 1 + random.randint(0, 3)
            if curr >= len(payouts):
                return 0
    num_simulations = 1000000
    total_payout = 0
    for _ in range(num_simulations):
        total_payout += simulate()
    return total_payout / num_simulations

N = int(input())
payouts = list(map(int, input().split()))
probs = []
for _ in range(N * (N + 1) // 2):
    probs.append(list(map(float, input().split())))
print(solve(N, payouts, probs))

