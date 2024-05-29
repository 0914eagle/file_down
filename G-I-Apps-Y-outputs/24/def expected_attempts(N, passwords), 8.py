
def expected_attempts(N, passwords):
    passwords.sort(key=lambda x: x[1], reverse=True)
    expected_attempts = 0
    cumulative_prob = 0
    
    for password, prob in passwords:
        expected_attempts += (1 + cumulative_prob) * prob
        cumulative_prob += prob
    
    return round(expected_attempts, 4)

# Input parsing
N = int(input())
passwords = [input().split() for _ in range(N)]
passwords = [(pw, float(prob)) for pw, prob in passwords]

# Output
print(expected_attempts(N, passwords))
```
