
def decipher_sentence(s, n, words):
    def is_valid(word, chars):
        if len(word) != len(chars):
            return False
        return all(c1 == c2 for c1, c2 in zip(word, chars))

    def dfs(s, words, deciphered):
        if not s:
            return deciphered
        for word in words:
            if is_valid(word, s[:len(word)]):
                result = dfs(s[len(word):], words, deciphered + [word])
                if result is not None:
                    return result
        return None

    decoded = dfs(s, words, [])
    if decoded is None:
        return "impossible"
    elif len(decoded) < len(s):
        return "ambiguous"
    else:
        return " ".join(decoded)

# Input parsing
sentence = input().strip()
num_words = int(input())
word_list = [input().strip() for _ in range(num_words)]

# Deciphering the sentence
result = decipher_sentence(sentence, num_words, word_list)
print(result)
```
