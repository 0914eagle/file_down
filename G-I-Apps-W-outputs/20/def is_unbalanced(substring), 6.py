
def is_unbalanced(substring):
    if len(substring) < 2:
        return False
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    max_count = max(char_counts.values())
    return max_count > len(substring) // 2

s = input().strip()
for i in range(len(s)):
    for j in range(i + 2, len(s) + 1):
        if is_unbalanced(s[i:j]):
            print(i + 1, j)
            exit()
print(-1, -1)
```
