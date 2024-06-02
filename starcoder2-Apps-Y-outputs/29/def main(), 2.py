
import sys

def main():
    a1, b1, a2, b2 = map(int, sys.stdin.readline().split())
    a3, b3, a4, b4 = map(int, sys.stdin.readline().split())

    # Gunnar's winning probability
    p1 = (b1 - a1 + 1) * (b2 - a2 + 1)
    p2 = (b3 - a3 + 1) * (b4 - a4 + 1)
    if p1 > p2:
        print("Gunnar")
    elif p1 < p2:
        print("Emma")
    else:
        print("Tie")

if __name__ == '__main__':
    main()

