
def translate_letter(letter, translations):
    for translation in translations:
        if letter == translation[0]:
            return translation[1]
    return letter

def translate_word(word, translations):
    translated_word = ''
    for letter in word:
        translated_word += translate_letter(letter, translations)
    return translated_word

def words_match(word1, word2, translations):
    if len(word1) != len(word2):
        return False
    translated_word1 = translate_word(word1, translations)
    translated_word2 = translate_word(word2, translations)
    return translated_word1 == translated_word2

m, n = map(int, input().split())
translations = [input().split() for _ in range(m)]

for _ in range(n):
    original_word, deciphered_word = input().split()
    if words_match(original_word, deciphered_word, translations):
        print("yes")
    else:
        print("no")
```
