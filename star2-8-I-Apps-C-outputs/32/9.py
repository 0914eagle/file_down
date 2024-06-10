
from itertools import permutations
n, r = map(int, input().split())
flights = [list(map(int, input().split())) for _ in range(r)]
f = int(input())
additional = [list(map(int, input().split())) for _ in range(f)]
cities = [i for i in range(1, n + 1)]
flight_dict = {}
for a, b, c in flights + additional:
    flight_dict[(a, b)] = c
    flight_dict[(b, a)] = c
paths = permutations(cities, n)
cost = float('inf')
for path in paths:
    curr_cost = 0
    for i in range(n):
        curr_cost += flight_dict[(path[i], path[(i + 1) % n])]
    cost = min(cost, curr_cost)
print(cost)

