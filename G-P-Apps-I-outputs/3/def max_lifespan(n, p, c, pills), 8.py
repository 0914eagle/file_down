
import heapq

def max_lifespan(n, p, c, pills):
    pills.sort(key=lambda x: x[0]) # Sort pills by introduction time
    max_age = [0] * (n + 1) # Initialize max age array
    
    # Initialize priority queue with tuple (max age, current time)
    pq = [(-c, 0)]
    
    for i in range(1, n + 1):
        max_age[i] = max(max_age[i], -pq[0][0] + i) # Update max age for current time
        while pq and pq[0][1] < i:
            heapq.heappop(pq) # Remove outdated pills from queue
        for pill_time, x, y in pills:
            if i >= pill_time:
                heapq.heappush(pq, (-max_age[pill_time] - c, pill_time + x)) # Add pill to queue
    
    return max(max_age)

# Input parsing
n, p, c = map(int, input().split())
pills = [list(map(int, input().split())) for _ in range(p)]

# Calculate and print the maximum lifespan
print('{:.9f}'.format(max_lifespan(n, p, c, pills)))
```
