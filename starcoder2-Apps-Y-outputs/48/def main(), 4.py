
import sys

def main():
    stock = 0
    cost = 0
    tax = 0.3
    for line in sys.stdin:
        line = line.split()
        if line[0] == 'buy':
            stock += int(line[1])
            cost += int(line[1]) * int(line[2])
        elif line[0] == 'sell':
            stock -= int(line[1])
            cost -= int(line[1]) * int(line[2])
        elif line[0] == 'split':
            cost *= int(line[1])
        elif line[0] == 'merge':
            cost /= int(line[1])
        elif line[0] == 'die':
            taxed = (int(line[1]) - cost / stock) * (1 - tax)
            print(stock * taxed)

if __name__ == '__main__':
    main()

