
import sys
from collections import defaultdict

def readline():
    return sys.stdin.readline().rstrip("\n")

def readlineasint():
    return int(readline())

def readlineasints():
    return map(int, readline().split())

def solve(juice_fractions):
    minimum_fractions = defaultdict(int)
    for a, b, c in juice_fractions:
        minimum_fractions["A"] = max(minimum_fractions["A"], a)
        minimum_fractions["B"] = max(minimum_fractions["B"], b)
        minimum_fractions["C"] = max(minimum_fractions["C"], c)
    satisfied_people = 0
    for a, b, c in juice_fractions:
        if a >= minimum_fractions["A"] and b >= minimum_fractions["B"] and c >= minimum_fractions["C"]:
            satisfied_people += 1
    return satisfied_people

def main():
    testcases = readlineasint()
    for t in range(testcases):
        n = readlineasint()
        juice_fractions = [list(readlineasints()) for _ in range(n)]
        print("Case #{}: {}".format(t+1, solve(juice_fractions)))

if __name__ == "__main__":
    main()

