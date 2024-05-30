
def translate_word(word, translations):
    translated_word = ''
    for letter in word:
        translated_letter = translations.get(letter, letter)
        translated_word += translated_letter
    return translated_word

def check_word_pair(word_pair, translations):
    original_word, deciphered_word = word_pair
    if len(original_word) != len(deciphered_word):
        return "no"
    translated_original = translate_word(original_word, translations)
    return "yes" if translated_original == deciphered_word else "no"

m, n = map(int, input().split())
translations = {}
for _ in range(m):
    a, b = input().split()
    translations[a] = b

for _ in range(n):
    word_pair = input().split()
    result = check_word_pair(word_pair, translations)
    print(result)
```
