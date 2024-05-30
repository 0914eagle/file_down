
def can_complete_jobs(n, jobs):
    current_time = 0
    for job in jobs:
        time_required, deadline = job
        if current_time + time_required > deadline:
            return "No"
        current_time += time_required
    return "Yes"

if __name__ == "__main__":
    n = int(input())
    jobs = [list(map(int, input().split())) for _ in range(n)]
    result = can_complete_jobs(n, jobs)
    print(result)
```
