
import sys

def solve(a):
    # your code here
    return 0

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))

if __name__ == "__main__":
    main()

