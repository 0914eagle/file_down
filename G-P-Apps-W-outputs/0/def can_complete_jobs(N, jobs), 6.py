
def can_complete_jobs(N, jobs):
    time = 0
    for job in jobs:
        a, b = job
        if time + a <= b:
            time += a
        else:
            return "No"
    return "Yes"

# Sample Input
N = 5
jobs = [(2, 4), (1, 9), (1, 8), (4, 9), (3, 12)]

# Check if Kizahashi can complete all jobs in time
result = can_complete_jobs(N, jobs)
print(result)
```
