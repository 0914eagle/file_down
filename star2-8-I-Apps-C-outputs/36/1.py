
from collections import deque

def get_minimum_hr_count(n, fired, hired):
    fired_workers = deque()
    hired_workers = deque()
    hr_count = 0
    hr_ids = []
    for i in range(n):
        for _ in range(fired[i]):
            fired_workers.append(hired_workers.popleft())
        for _ in range(hired[i]):
            hired_workers.append(i + 1)
        while len(set(hired_workers)) != len(hired_workers):
            hired_workers.popleft()
        if len(hired_workers) > hr_count:
            hr_count = len(hired_workers)
        hr_ids.append(hired_workers[0])
        
    return hr_count, hr_ids


n = int(input())
fired = []
hired = []
for _ in range(n):
    f, h = map(int, input().split())
    fired.append(f)
    hired.append(h)
    
hr_count, hr_ids = get_minimum_hr_count(n, fired, hired)
print(hr_count)
print(' '.join(map(str, hr_ids)))

