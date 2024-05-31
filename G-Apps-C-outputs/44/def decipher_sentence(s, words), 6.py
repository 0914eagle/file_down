
def decipher_sentence(s, words):
    n = len(s)
    dp = [''] * (n + 1)
    dp[0] = ' '
    
    for i in range(1, n + 1):
        for word in words:
            if i >= len(word) and s[i-len(word):i] == word and dp[i-len(word)] != None:
                if dp[i] == '':
                    dp[i] = word
                else:
                    dp[i] = None
                    break
    
    if dp[-1] is None:
        return "ambiguous"
    elif dp[-1] == '':
        return "impossible"
    else:
        result = []
        i = n
        while i > 0:
            result.append(dp[i])
            i -= len(dp[i])
        return ' '.join(result[::-1])

# Input reading
sentence = input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]

# Decipher the sentence
deciphered_sentence = decipher_sentence(sentence, words)
print(deciphered_sentence)
