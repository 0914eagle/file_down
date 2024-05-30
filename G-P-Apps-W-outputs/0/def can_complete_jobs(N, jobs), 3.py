
def can_complete_jobs(N, jobs):
    current_time = 0
    for a, b in jobs:
        if current_time + a <= b:
            current_time += a
        else:
            return "No"
    return "Yes"

# Read input
N = int(input())
jobs = [list(map(int, input().split())) for _ in range(N)]

# Check if Kizahashi can complete all jobs in time
result = can_complete_jobs(N, jobs)
print(result)
```
