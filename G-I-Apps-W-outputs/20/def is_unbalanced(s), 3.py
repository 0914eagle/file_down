
def is_unbalanced(s):
    for i in range(len(s)):
        count = {}
        for j in range(i, len(s)):
            if s[j] in count:
                count[s[j]] += 1
            else:
                count[s[j]] = 1
            if len(set(count.values())) == 1 and max(count.values()) > (j - i + 1) / 2:
                return i + 1, j + 1
    return -1, -1

s = input().strip()
result = is_unbalanced(s)
print(*result)
```
