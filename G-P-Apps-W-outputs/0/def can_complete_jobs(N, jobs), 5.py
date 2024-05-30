
def can_complete_jobs(N, jobs):
    current_time = 0
    for job in jobs:
        time_to_complete = job[0]
        deadline = job[1]
        if current_time + time_to_complete > deadline:
            return "No"
        current_time += time_to_complete
    return "Yes"

# Read input
N = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(N)]

# Check if Kizahashi can complete all the jobs in time
result = can_complete_jobs(N, jobs)
print(result)
```
