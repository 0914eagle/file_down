
import sys

def solve_hacking_passwords():
    n = int(sys.stdin.readline())
    passwords = []
    for _ in range(n):
        password, probability = sys.stdin.readline().split()
        passwords.append((password, float(probability)))

    passwords.sort(key=lambda x: x[1], reverse=True)

    expected_attempts = 0
    cumulative_probability = 0
    for i in range(n):
        password, probability = passwords[i]
        expected_attempts += (i + 1) * probability
        cumulative_probability += probability
        if cumulative_probability == 1:
            break

    return round(expected_attempts, 4)

print(solve_hacking_passwords())
```
