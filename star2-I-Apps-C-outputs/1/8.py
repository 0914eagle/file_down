
from math import sqrt
def solve(n, lights):
    pass

def main():
    n = int(input())
    lights = [list(map(int, input().split())) for _ in range(n-1)]
    print(solve(n, lights))

if __name__ == '__main__':
    main()

