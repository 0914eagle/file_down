
def decipher_sentence(s, words):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for word in words:
            if i >= len(word) and dp[i - len(word)] and sorted(s[i - len(word):i]) == sorted(word):
                dp[i] = True

    if not dp[n]:
        return "impossible"

    result = []
    i = n
    while i > 0:
        for word in words:
            if i >= len(word) and dp[i - len(word)] and sorted(s[i - len(word):i]) == sorted(word):
                result.append(word)
                i -= len(word)
                break

    if len(result) < n:
        return "ambiguous"
    else:
        return " ".join(result[::-1])

s = "tihssnetnceemkaesprfecetsesne"
n = 5
words = ["makes", "perfect", "sense", "sentence", "this"]

print(decipher_sentence(s, words))
