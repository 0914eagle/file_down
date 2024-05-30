
def can_complete_jobs(N, jobs):
    jobs.sort(key=lambda x: x[1])  # Sort jobs by deadline
    current_time = 0

    for job in jobs:
        current_time += job[0]
        if current_time > job[1]:
            return "No"
    
    return "Yes"

# Input parsing
N = int(input())
jobs = []
for _ in range(N):
    A, B = map(int, input().split())
    jobs.append((A, B))

# Check if Kizahashi can complete all jobs in time
result = can_complete_jobs(N, jobs)
print(result)
```
