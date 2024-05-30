
def translate_letter(letter, translations):
    if letter in translations:
        return translations[letter]
    else:
        return letter

def translate_word(word, translations):
    translated_word = ""
    for letter in word:
        translated_word += translate_letter(letter, translations)
    return translated_word

def check_word_pair(word1, word2, translations):
    if len(word1) != len(word2):
        return "no"
    
    for i in range(len(word1)):
        translated_letter = translate_letter(word1[i], translations)
        if translated_letter != word2[i]:
            return "no"
    
    return "yes"

m, n = map(int, input().split())
translations = {}
for _ in range(m):
    a, b = input().split()
    translations[a] = b

for _ in range(n):
    word1, word2 = input().split()
    print(check_word_pair(word1, word2, translations))
```
