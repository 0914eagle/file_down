
import math

def distance_to_edge(x, y):
    return min(x, 10000-x, y, 10000-y)

def solve_round_table(N, sticks):
    stick_labels = list(range(1, N+1))
    stick_labels.sort(key=lambda label: distance_to_edge((sticks[label-1][0]+sticks[label-1][2])/2, (sticks[label-1][1]+sticks[label-1][3])/2))
    return ' '.join(map(str, stick_labels))

# Input parsing
N = int(input())
sticks = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    sticks.append((x1, y1, x2, y2))

# Solve the problem and output the result
result = solve_round_table(N, sticks)
print(result)
