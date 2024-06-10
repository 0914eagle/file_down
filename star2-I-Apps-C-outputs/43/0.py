
import sys
import random

def main():
    N = int(sys.stdin.readline())
    payout = [float(x) for x in sys.stdin.readline().split()]
    prob = [[float(x) for x in sys.stdin.readline().split()] for _ in range(N*(N+1)//2)]
    
    def simulate_game():
        current_hole = 0
        while True:
            current_prob = prob[current_hole]
            r = random.random()
            if r < current_prob[0]:
                current_hole -= N
            elif r < current_prob[0] + current_prob[1]:
                current_hole -= N + 1
            elif r < current_prob[0] + current_prob[1] + current_prob[2]:
                current_hole += N - 1
            elif r < current_prob[0] + current_prob[1] + current_prob[2] + current_prob[3]:
                current_hole += N
            elif r < current_prob[0] + current_prob[1] + current_prob[2] + current_prob[3] + current_prob[4]:
                return payout[current_hole]
    
    total_payout = 0
    num_simulations = 100000
    for _ in range(num_simulations):
        total_payout += simulate_game()
    
    print(total_payout / num_simulations)
    
if __name__ == '__main__':
    main()

