
import heapq

def expected_attempts(N, passwords):
    heap = [(1 / prob, prob) for _, prob in passwords]  # Convert probabilities to time needed to crack password
    heapq.heapify(heap)
    
    total_time = 0
    while len(heap) > 1:
        time1, prob1 = heapq.heappop(heap)
        time2, prob2 = heapq.heappop(heap)
        
        total_time += time1 + time2 * prob1
        new_prob = prob1 + prob2
        heapq.heappush(heap, (time1 + time2, new_prob))
    
    return total_time

# Input reading
N = int(input())
passwords = []
for _ in range(N):
    password, prob = input().split()
    passwords.append((password, float(prob)))

# Calculate and output the expected number of attempts
result = expected_attempts(N, passwords)
print(f"{result:.4f}")
```
