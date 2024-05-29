
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_sequence_present(n, m, k, sequence):
    for i in range(1, n + 1):
        row = [gcd(i, j) for j in range(1, m + 1)]
        for j in range(1, m - k + 2):
            if row[j - 1:j + k - 1] == sequence:
                return "YES"
    return "NO"

n, m, k = map(int, input().split())
sequence = list(map(int, input().split()))

print(is_sequence_present(n, m, k, sequence))
```
