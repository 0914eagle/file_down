
import sys

def main():
    a1, b1, a2, b2 = [int(x) for x in sys.stdin.readline().split()]
    a3, b3, a4, b4 = [int(x) for x in sys.stdin.readline().split()]

    if a1 + b1 > a3 + b3:
        print("Gunnar")
    elif a1 + b1 < a3 + b3:
        print("Emma")
    else:
        print("Tie")

if __name__ == "__main__":
    main()

