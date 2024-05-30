
MOD = 998244353

def count_monotonic_renumerations(n, a):
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    counts = list(freq.values())
    counts.sort()

    result = 1
    current_count = 1
    for i in range(1, len(counts)):
        if counts[i] == counts[i - 1]:
            current_count += 1
        else:
            for j in range(1, current_count + 1):
                result = (result * j) % MOD
            current_count = 1

    for j in range(1, current_count + 1):
        result = (result * j) % MOD

    return result

# Read input
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the result
print(count_monotonic_renumerations(n, a))
```
