
import sys

def main():
    n = int(sys.stdin.readline())
    shares = 0
    cost = 0
    for i in range(n):
        line = sys.stdin.readline().split()
        if line[0] == "buy":
            shares += int(line[1])
            cost += int(line[1]) * int(line[2])
        elif line[0] == "sell":
            shares -= int(line[1])
            cost -= int(line[1]) * int(line[2])
        elif line[0] == "split":
            cost *= int(line[1])
        elif line[0] == "merge":
            cost //= int(line[1])
        elif line[0] == "die":
            print(shares * (int(line[1]) - cost / shares * 0.3))

main()

