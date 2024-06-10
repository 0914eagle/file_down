
from sys import stdin

def main():
    m, n = map(int, stdin.readline().split())
    if m >= 8:
        print("satisfactory")
    else:
        print("unsatisfactory")

main()

