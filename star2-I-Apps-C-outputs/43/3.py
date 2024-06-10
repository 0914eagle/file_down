
import sys
import random

def main():
    N = int(sys.stdin.readline())
    payout = [float(x) for x in sys.stdin.readline().split()]
    prob = [[float(x) for x in sys.stdin.readline().split()] for _ in range(N*(N+1)//2)]
    
    def simulate(payout, prob):
        curr = 0
        while True:
            p = random.random()
            if p < prob[curr][4]:
                return payout[curr]
            p -= prob[curr][4]
            if p < prob[curr][0]:
                curr -= N
            elif p < prob[curr][0] + prob[curr][1]:
                curr -= N + 1
            elif p < prob[curr][0] + prob[curr][1] + prob[curr][2]:
                curr += N - 1
            else:
                curr += N
    
    num_sim = 100000
    total_payout = 0
    for _ in range(num_sim):
        total_payout += simulate(payout, prob)
    
    print(total_payout / num_sim)
    
if __name__ == "__main__":
    main()

