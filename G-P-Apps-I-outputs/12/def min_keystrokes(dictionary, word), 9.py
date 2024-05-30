
def min_keystrokes(dictionary, word):
    n = len(word)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i-1] + 1  # Typing the next character
        for d in dictionary:
            if d.startswith(word[:i]):
                dp[i] = min(dp[i], i + 1 + dp[i-len(d)])  # Tab, delete, type the rest
    return dp[n]

n, m = map(int, input().split())
dictionary = [input().strip() for _ in range(n)]
words_to_type = [input().strip() for _ in range(m)]

for word in words_to_type:
    print(min_keystrokes(dictionary, word))
```
