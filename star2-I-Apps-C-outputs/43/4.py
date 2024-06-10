
import sys
import random

def simulate(machine, payouts):
    row = 0
    col = 0
    while True:
        payout = payouts[row][col]
        if payout != 0:
            return payout
        probs = machine[row][col]
        r = random.random()
        if r < probs[0]:
            row -= 1
            col -= 1
        elif r < probs[0] + probs[1]:
            row -= 1
            col += 1
        elif r < probs[0] + probs[1] + probs[2]:
            row += 1
            col -= 1
        elif r < probs[0] + probs[1] + probs[2] + probs[3]:
            row += 1
            col += 1
        else:
            return 0

def main():
    N = int(sys.stdin.readline())
    payouts = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    machine = [[list(map(float, sys.stdin.readline().split())) for _ in range(N)] for N in range(1, N+1)]
    num_samples = 100000
    total_payout = 0
    for _ in range(num_samples):
        total_payout += simulate(machine, payouts)
    print(total_payout / num_samples)

main()

