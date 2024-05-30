
def can_complete_jobs(N, jobs):
    time = 0
    for i in range(N):
        A, B = jobs[i]
        if time + A > B:
            return "No"
        time += A
    return "Yes"

# Input processing
N = int(input())
jobs = []
for _ in range(N):
    A, B = map(int, input().split())
    jobs.append((A, B))

# Check if Kizahashi can complete all jobs in time
result = can_complete_jobs(N, jobs)
print(result)
```
