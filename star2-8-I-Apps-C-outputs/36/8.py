
from collections import deque
from sys import stdin
def readline():
    return next(stdin).strip()
n = int(readline())
fired = [0] * (n + 1)
hired = [0] * (n + 1)
for i in range(n):
    f, h = map(int, readline().split())
    fired[i + 1] = fired[i] + f
    hired[i + 1] = hired[i] + h
fire_queue = deque(range(1, n + 1))
hr_assignments = [0] * (n + 1)
current_hr = 1
for i in range(1, n + 1):
    if fired[i] > 0:
        while fired[i] > 0:
            hr_assignments[fire_queue.popleft()] = current_hr
            fired[i] -= 1
        current_hr += 1
    if hired[i] > 0:
        for j in range(i, n + 1):
            if hr_assignments[j] == 0:
                hr_assignments[j] = current_hr
                hired[i] -= 1
            if hired[i] == 0:
                break
        current_hr += 1
print(current_hr - 1)
print(*hr_assignments[1:])

