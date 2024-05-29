
import heapq

def expected_attempts(N, passwords):
    passwords.sort(key=lambda x: x[1], reverse=True)
    attempts = 0
    total_prob = 0
    for password, prob in passwords:
        attempts += (1 + total_prob) * prob
        total_prob += prob
    return round(attempts, 4)

# Read input
N = int(input())
passwords = []
for _ in range(N):
    password, prob = input().split()
    passwords.append((password, float(prob)))

# Calculate and print expected number of attempts
result = expected_attempts(N, passwords)
print(result)
