
import heapq

def expected_attempts(N, passwords):
    passwords.sort(key=lambda x: -x[1])
    total_attempts = 0
    for i, (_, prob) in enumerate(passwords):
        total_attempts += (i + 1) * prob
    return total_attempts

# Input
N = int(input())
passwords = []
for _ in range(N):
    pwd, prob = input().split()
    passwords.append((pwd, float(prob)))

# Output
print("{:.4f}".format(expected_attempts(N, passwords)))
