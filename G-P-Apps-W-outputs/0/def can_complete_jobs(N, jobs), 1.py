
def can_complete_jobs(N, jobs):
    jobs.sort(key=lambda x: x[1])  # Sort jobs by deadline
    current_time = 0

    for i in range(N):
        current_time += jobs[i][0]  # Time taken to complete current job
        if current_time > jobs[i][1]:  # Check if deadline is exceeded
            return "No"

    return "Yes"

# Sample Input
N = 5
jobs = [(2, 4), (1, 9), (1, 8), (4, 9), (3, 12)]

print(can_complete_jobs(N, jobs))  # Output: Yes
```
