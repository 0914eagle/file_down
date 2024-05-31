
def decipher_sentence(sentence, words):
    sentence = list(sentence)
    words = set(words)
    n = len(sentence)

    dp = [None] * (n + 1)
    dp[0] = []

    for i in range(1, n + 1):
        dp[i] = []
        for j in range(i):
            if dp[j] is not None and sentence[j:i] in words:
                if dp[i] is None or len(dp[j]) + 1 < len(dp[i]):
                    dp[i] = dp[j] + [sentence[j:i]]

    if dp[n] is None:
        return "impossible"
    elif len(dp[n]) > 1:
        return "ambiguous"
    else:
        return " ".join(dp[n])

# Reading input
sentence = input().strip()
n = int(input().strip())
words = set([input().strip() for _ in range(n)])

# Output
result = decipher_sentence(sentence, words)
print(result)
