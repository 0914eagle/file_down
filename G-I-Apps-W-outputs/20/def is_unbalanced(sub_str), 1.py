
def is_unbalanced(sub_str):
    if len(sub_str) < 2:
        return False
    counts = {}
    for char in sub_str:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    max_count = max(counts.values())
    return max_count > len(sub_str) / 2

def find_unbalanced_substring(s):
    for start in range(len(s)):
        for end in range(start + 2, len(s) + 1):
            sub_str = s[start:end]
            if is_unbalanced(sub_str):
                return start + 1, end
    return -1, -1

s = input().strip()
start, end = find_unbalanced_substring(s)
print(start, end)
```
