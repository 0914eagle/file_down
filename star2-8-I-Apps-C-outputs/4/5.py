
import sys

def solve(case_num, fruits):
    total = 0
    for fruit in fruits:
        if fruit[0] > 0:
            total += 1
    print(f"Case #{case_num}: {total}")

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        fruits = []
        for _ in range(n):
            fruits.append(tuple(map(int, sys.stdin.readline().split())))
        solve(i + 1, fruits)

if __name__ == "__main__":
    main()

