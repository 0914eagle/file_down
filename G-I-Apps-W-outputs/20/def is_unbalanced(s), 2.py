
def is_unbalanced(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1, n):
            substring = s[i:j+1]
            if len(substring) >= 2:
                count = {}
                for char in substring:
                    if char in count:
                        count[char] += 1
                    else:
                        count[char] = 1
                max_count = max(count.values())
                if max_count > len(substring) / 2:
                    return i+1, j+1
    return -1, -1

s = input()
result = is_unbalanced(s)
print(result[0], result[1])
```

