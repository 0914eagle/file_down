
def decipher_sentence(sentence, words):
    def is_valid_mapping(mapping, sentence, words):
        decoded = ""
        for word in sentence.split():
            if len(word) not in mapping:
                return False
            decoded += words[mapping[len(word)]] + " "
        return decoded.strip()

    def backtrack(mapping, idx, sentence, words):
        if idx == len(sentence):
            return is_valid_mapping(mapping, sentence, words)

        for i in range(len(words)):
            if i not in mapping.values():
                mapping[idx] = i
                result = backtrack(mapping, idx + 1, sentence, words)
                if result:
                    return result
                mapping.pop(idx)

        return None

    words = sorted(words, key=len, reverse=True)
    mapping = {}
    result = backtrack(mapping, 0, sentence, words)
    return result if result else "impossible"

# Input parsing
sentence = input().strip()
n = int(input().strip())
words = [input().strip() for _ in range(n)]

deciphered_sentence = decipher_sentence(sentence, words)
print(deciphered_sentence if deciphered_sentence else "ambiguous")
```
