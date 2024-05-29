
def is_unbalanced(substring):
    length = len(substring)
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    max_count = max(char_count.values())
    return length >= 2 and max_count > length / 2

def find_unbalanced_substring(s):
    for i in range(len(s) - 1):
        for j in range(i + 2, len(s) + 1):
            if is_unbalanced(s[i:j]):
                return i + 1, j

    return -1, -1

s = input().strip()
result = find_unbalanced_substring(s)
print(result[0], result[1])
```
