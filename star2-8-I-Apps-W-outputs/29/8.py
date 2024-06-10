
from math import floor, ceil


def solve_update_query(a, b):
    global left, right
    left = min(left, a - b)
    right = max(right, a - b)


def solve_evaluation_query():
    if left == right:
        print(left, left)
    elif left > right:
        print("No solutions")
    else:
        x = floor(left)
        y = ceil(left)
        if abs(x - left) <= abs(y - left):
            print(x, x)
        else:
            print(y, y)


q = int(input())
left = float("inf")
right = float("-inf")
for _ in range(q):
    query = input()
    if query[0] == "1":
        a, b = map(int, query.split()[1:])
        solve_update_query(a, b)
    else:
        solve_evaluation_query()

