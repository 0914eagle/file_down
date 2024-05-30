
def decipher_sentence(sentence, words):
    def is_valid(s):
        for i in range(len(s)):
            word = s[0] + ''.join(sorted(s[1:i], key=lambda x: s.index(x))) + s[i:]
            if word in words:
                return True
        return False
    
    def backtrack(s, decoded):
        if not s:
            return decoded
        
        for i in range(1, len(s)):
            word = s[0] + ''.join(sorted(s[1:i], key=lambda x: s.index(x))) + s[i:]
            if word in words:
                new_decoded = decoded + [word]
                result = backtrack(s[i:], new_decoded)
                if result:
                    return result
        
        return None
    
    decoded_sentence = backtrack(sentence, [])
    
    if decoded_sentence:
        return ' '.join(decoded_sentence)
    else:
        return 'impossible'

# Input parsing
input_sentence = input().strip()
n = int(input().strip())
dictionary = []
for i in range(n):
    dictionary.append(input().strip())

# Decipher the sentence
result = decipher_sentence(input_sentence, dictionary)
if result:
    print(result)
else:
    print('ambiguous')
```
