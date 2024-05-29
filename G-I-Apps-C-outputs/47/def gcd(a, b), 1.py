
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_sequence_in_table(n, m, k, sequence):
    for i in range(1, n + 1):
        found = False
        for j in range(1, m - k + 2):
            valid = True
            for l in range(1, k + 1):
                if gcd(i, j + l - 1) != sequence[l - 1]:
                    valid = False
                    break
            if valid:
                found = True
                break
        if found:
            return "YES"
    return "NO"

n, m, k = map(int, input().split())
sequence = list(map(int, input().split()))

result = is_sequence_in_table(n, m, k, sequence)
print(result)
```
