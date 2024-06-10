
from sys import stdin
def solve():
    n, c = map(int, stdin.readline().split())
    w = list(map(int, stdin.readline().split()))
    fruits_ate = set()
    total_weight = 0
    for weight in w:
        if total_weight + weight <= c:
            total_weight += weight
            fruits_ate.add(weight)
    return len(fruits_ate)
print(solve())

