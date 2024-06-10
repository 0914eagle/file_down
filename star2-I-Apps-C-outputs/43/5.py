
import sys
import random

def main():
    n = int(sys.stdin.readline())
    payout = [float(x) for x in sys.stdin.readline().split()]
    prob = [[float(x) for x in sys.stdin.readline().split()] for _ in range(n * (n + 1) // 2)]
    total_payout = 0.0
    for _ in range(1000000):
        curr_payout = 0.0
        curr_hole = 0
        while True:
            curr_payout += payout[curr_hole]
            if random.random() < prob[curr_hole][4]:
                break
            curr_hole += 1
            curr_prob = [prob[curr_hole][0], prob[curr_hole][1], prob[curr_hole][2], prob[curr_hole][3]]
            curr_hole += random.choices(range(4), weights=curr_prob)[0]
        total_payout += curr_payout
    print(total_payout / 1000000)

if __name__ == "__main__":
    main()

