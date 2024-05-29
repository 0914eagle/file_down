
def is_unbalanced(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 2, n + 1):
            substring = s[i:j]
            if len(substring) > 1:
                count = {}
                for char in substring:
                    if char in count:
                        count[char] += 1
                    else:
                        count[char] = 1

                max_count = max(count.values())
                if max_count > len(substring) // 2:
                    return i + 1, j

    return -1, -1

# Sample Input
s = "needed"
a, b = is_unbalanced(s)
print(a, b)
```
