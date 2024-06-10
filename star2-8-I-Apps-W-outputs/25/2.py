
from sys import stdin
input_iter = iter(stdin.read().split())
def input():
    global input_iter
    return next(input_iter)

def main():
    n, m, k = map(int, input().split())
    buildings = [0] * m
    for _ in range(n):
        buildings[int(input()) - 1] += 1
    buildings.sort(reverse=True)
    if k >= m:
        print(sum(buildings))
    else:
        print(sum(buildings[:k]) + sum(buildings[k:] * 2))


if __name__ == '__main__':
    main()

