
def can_complete_jobs(N, jobs):
    current_time = 0
    for job in jobs:
        time_needed, deadline = job
        current_time += time_needed
        if current_time > deadline:
            return "No"
    return "Yes"

# Reading input
N = int(input())
jobs = []
for _ in range(N):
    A, B = map(int, input().split())
    jobs.append((A, B))

# Checking if Kizahashi can complete all jobs in time
result = can_complete_jobs(N, jobs)
print(result)
```
