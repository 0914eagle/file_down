
import sys

def expected_attempts(N, passwords):
    passwords.sort(key=lambda x: x[1], reverse=True)
    expected_attempts = 0
    cumulative_prob = 0
    
    for i, (password, prob) in enumerate(passwords):
        expected_attempts += (i+1) * prob
        cumulative_prob += prob
        if cumulative_prob >= 1:
            break
    
    return expected_attempts

if __name__ == "__main__":
    N = int(input())
    passwords = []
    for _ in range(N):
        password, prob = input().split()
        passwords.append((password, float(prob)))
    
    result = expected_attempts(N, passwords)
    print("{:.4f}".format(result))
```
