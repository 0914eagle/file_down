
def decipher_sentence(s, n, words):
    def is_valid(deciphered):
        words_set = set(words)
        words_found = set()
        text = ''.join(deciphered)
        text_words = text.split(' ')
        
        for word in text_words:
            if word not in words_set:
                return False
            words_found.add(word)
        
        return words_found == words_set

    def backtrack(index, deciphered):
        if index == len(s):
            if is_valid(deciphered):
                return deciphered
            else:
                return None

        for i in range(index, len(s)):
            word = s[index:i+1]
            if word in words:
                result = backtrack(i+1, deciphered + [word, ' '])
                if result:
                    return result
    
    result = backtrack(0, [])
    if result:
        return ''.join(result).strip()
    else:
        return "impossible"

# Input
s = input().strip()
n = int(input().strip())
words = set(input().strip() for _ in range(n))

# Output
deciphered_sentence = decipher_sentence(s, n, words)
if deciphered_sentence:
    print(deciphered_sentence)
else:
    print("ambiguous")

