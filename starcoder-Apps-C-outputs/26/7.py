
from collections import deque

n = int(input())
field = list(input())
queue = deque()
for i in range(n):
    if field[i] == 'P':
        queue.append((i, 0))
while True:
    x, c = queue.popleft()
    if field[x] == '*':
        field[x] = '.'
        print(c)
        break
    if x > 0 and field[x - 1] != '.':
        queue.append((x - 1, c + 1))
        field[x - 1] = '.'
    if x < n - 1 and field[x + 1] != '.':
        queue.append((x + 1, c + 1))
        field[x + 1] = '.'
