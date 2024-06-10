
import random
import math

def solve(N, payout, prob):
    payout = payout[:]
    prob = prob[:]
    
    def simulate():
        cur = 0
        while True:
            if payout[cur] != 0:
                return payout[cur]
            r = random.random()
            if r < prob[cur][4]:
                return payout[cur]
            r -= prob[cur][4]
            if r < prob[cur][0]:
                cur -= N + 1
            elif r < prob[cur][0] + prob[cur][1]:
                cur -= N
            elif r < prob[cur][0] + prob[cur][1] + prob[cur][2]:
                cur += 1
            else:
                cur += N + 1
    
    num_sim = 100000
    total_payout = 0
    for _ in range(num_sim):
        total_payout += simulate()
    
    return total_payout / num_sim

N = int(input())
payout = list(map(int, input().split()))
prob = []
for _ in range(N * (N + 1) // 2):
    prob.append(list(map(float, input().split())))

print(solve(N, payout, prob))

