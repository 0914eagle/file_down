
def is_unbalanced(s):
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            if len(substring) >= 2:
                char_count = {}
                for char in substring:
                    if char in char_count:
                        char_count[char] += 1
                    else:
                        char_count[char] = 1
                most_common_char = max(char_count, key=char_count.get)
                if char_count[most_common_char] > len(substring) / 2:
                    return i + 1, j
    return -1, -1

s = input().strip()
result = is_unbalanced(s)
print(result[0], result[1])
```
