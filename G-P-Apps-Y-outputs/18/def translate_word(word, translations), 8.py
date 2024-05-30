
def translate_word(word, translations):
    translated_word = ""
    for letter in word:
        translated_letter = translations.get(letter, letter)
        translated_word += translated_letter
    return translated_word

def check_word_pair(word1, word2, translations):
    if len(word1) != len(word2):
        return "no"
    for i in range(len(word1)):
        translated_word1 = translate_word(word1, translations)
        translated_word2 = translate_word(word2, translations)
        if translated_word1 != translated_word2:
            return "no"
    return "yes"

m, n = map(int, input().split())
translations = {}
for _ in range(m):
    a, b = input().split()
    translations[a] = b

for _ in range(n):
    word1, word2 = input().split()
    result = check_word_pair(word1, word2, translations)
    print(result)
```
