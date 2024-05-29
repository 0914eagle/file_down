
def expected_attempts(passwords):
    sorted_passwords = sorted(passwords, key=lambda x: x[1], reverse=True)
    attempts = 0
    current_probability = 1
    for _, probability in sorted_passwords:
        attempts += current_probability * probability
        current_probability *= (1 - probability)
    return round(attempts, 4)

# Input
n = int(input())
passwords = [input().split() for _ in range(n)]
passwords = [(password, float(prob)) for password, prob in passwords]

# Output
print(expected_attempts(passwords))
```
