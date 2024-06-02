
import sys

def main():
    n = int(sys.stdin.readline())
    total_shares = 0
    total_cost = 0.0
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        if line[0] == 'buy':
            shares = int(line[1])
            cost = int(line[2])
            total_shares += shares
            total_cost += shares * cost
        elif line[0] == 'sell':
            shares = int(line[1])
            cost = int(line[2])
            total_shares -= shares
            total_cost -= shares * cost
        elif line[0] == 'split':
            x = int(line[1])
            total_shares *= x
            total_cost /= x
        elif line[0] == 'merge':
            x = int(line[1])
            total_shares /= x
            total_cost *= x
        elif line[0] == 'die':
            cost = int(line[1])
            tax_rate = 0.3
            tax = total_cost * tax_rate
            total_cost = total_shares * cost - tax
            print(total_cost)

if __name__ == '__main__':
    main()

