
import sys

def min_cost_path(t, test_cases):
    for i in range(t):
        x, y = test_cases[i][0]
        costs = test_cases[i][1]

        min_cost = min(
            abs(x) * costs[0] + abs(y) * costs[1],
            abs(x - y) * costs[2] + min(x, y) * costs[3],
            abs(y - x) * costs[4] + min(x, y) * costs[5]
        )

        print(min_cost)

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    x, y = map(int, input().split())
    costs = list(map(int, input().split()))
    test_cases.append(((x, y), costs))

# Call the function
min_cost_path(t, test_cases)
