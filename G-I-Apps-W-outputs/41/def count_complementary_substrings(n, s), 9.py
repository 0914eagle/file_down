
def count_complementary_substrings(n, s):
    def is_complementary(a, b):
        return (a == 'A' and b == 'T') or (a == 'T' and b == 'A') or (a == 'C' and b == 'G') or (a == 'G' and b == 'C')

    def count_permutations(string):
        from collections import Counter
        counter = Counter(string)
        return math.factorial(len(string)) // (math.prod(math.factorial(value) for value in counter.values()))

    import math

    total_count = 0
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            substring = s[start:start + length]
            for i in range(len(substring)):
                for j in range(i + 1, len(substring)):
                    if is_complementary(substring[i], substring[j]):
                        if count_permutations(substring) > 0:
                            total_count += 1
                            break

    return total_count

# Input processing
n, s = input().split()
n = int(n)
result = count_complementary_substrings(n, s)
print(result)
```
