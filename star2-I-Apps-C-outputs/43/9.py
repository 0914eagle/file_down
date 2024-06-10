
import sys
import random

def main():
    N = int(sys.stdin.readline())
    payout = [int(x) for x in sys.stdin.readline().split()]
    prob = [[float(x) for x in sys.stdin.readline().split()] for i in range(N * (N + 1) // 2)]
    total_prob = [0.0] * (N * (N + 1) // 2)
    for i in range(N * (N + 1) // 2):
        total_prob[i] = sum(prob[i])
    num_simulations = 100000
    total_payout = 0.0
    for i in range(num_simulations):
        current_hole = 0
        current_payout = 0.0
        while True:
            current_payout += payout[current_hole]
            if random.random() < total_prob[current_hole]:
                break
            rand = random.random()
            if rand < prob[current_hole][0]:
                current_hole -= N + 1
            elif rand < prob[current_hole][0] + prob[current_hole][1]:
                current_hole -= N
            elif rand < prob[current_hole][0] + prob[current_hole][1] + prob[current_hole][2]:
                current_hole += 1
            else:
                current_hole += N + 1
        total_payout += current_payout
    print(total_payout / num_simulations)

main()

