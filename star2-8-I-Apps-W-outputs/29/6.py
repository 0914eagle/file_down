
from collections import deque
from math import ceil, floor

def eval_query(a, b):
    x = ceil(a - b)
    print(x, int(a * x - b * (x + 1) // 2))

def update_query(a, b):
    global left, right
    left += a
    right += b

q = int(input())
left = right = 0
queries = deque()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        update_query(*query[1:])
    else:
        queries.append(query[1:])

while queries:
    eval_query(*queries.popleft())

