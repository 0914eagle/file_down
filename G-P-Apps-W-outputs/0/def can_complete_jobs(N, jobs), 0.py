
def can_complete_jobs(N, jobs):
    jobs.sort(key=lambda x: x[1])  # Sort the jobs by deadline
    
    time = 0
    for job in jobs:
        time += job[0]
        if time > job[1]:  # If Kizahashi exceeds the deadline, return "No"
            return "No"
    
    return "Yes"

# Input processing
N = int(input())
jobs = []
for _ in range(N):
    A, B = map(int, input().split())
    jobs.append((A, B))

# Check if Kizahashi can complete all the jobs in time
result = can_complete_jobs(N, jobs)
print(result)
```
