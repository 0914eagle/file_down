
def decipher_sentence(s, words):
    def is_valid_sentence(sentence, word_set):
        words = sentence.split()
        for word in words:
            if word not in word_set:
                return False
        return True

    def decode_word(word):
        return ''.join([word[0]] + list(word[1:-1])[::-1] + [word[-1]])

    word_set = set(words)
    decoded_sentence = []
    for word in s.split():
        decoded_word = decode_word(word)
        if decoded_word in word_set:
            decoded_sentence.append(decoded_word)
        else:
            return "impossible"
    
    if is_valid_sentence(' '.join(decoded_sentence), word_set):
        return ' '.join(decoded_sentence)
    else:
        return "ambiguous"

# Input processing
s = input().strip()
n = int(input().strip())
words = [input().strip() for _ in range(n)]

# Output
print(decipher_sentence(s, words))
```
