
def expected_attempts(N, passwords):
    passwords.sort(key=lambda x: x[1], reverse=True)
    expected_attempts = 0
    cumulative_probability = 0

    for password, probability in passwords:
        expected_attempts += (1 + cumulative_probability) * probability
        cumulative_probability += probability

    return round(expected_attempts, 4)

# Input processing
N = int(input())
passwords = []

for _ in range(N):
    p, prob = input().split()
    passwords.append((p, float(prob)))

# Call the function and output the result
result = expected_attempts(N, passwords)
print(result)
```
