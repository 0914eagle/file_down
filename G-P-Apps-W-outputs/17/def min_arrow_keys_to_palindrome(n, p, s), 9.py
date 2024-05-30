
def min_arrow_keys_to_palindrome(n, p, s):
    p -= 1  # 0-based indexing
    mid = n // 2
    total_presses = 0

    for i in range(mid):
        left_distance = (p - i + n) % n
        right_distance = (p + i) % n

        if s[left_distance] != s[right_distance]:
            min_presses = min(abs(ord(s[left_distance]) - ord(s[right_distance])), 26 - abs(ord(s[left_distance]) - ord(s[right_distance]))
            total_presses += min_presses

    return total_presses

# Input processing
n, p = map(int, input().split())
s = input().strip()

result = min_arrow_keys_to_palindrome(n, p, s)
print(result)
```
