
def complete_jobs_on_time(N, jobs):
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
    a, b = map(int, input().split())
    jobs.append((a, b))

# Check if Kizahashi can complete all jobs in time
result = complete_jobs_on_time(N, jobs)
print(result)
```
