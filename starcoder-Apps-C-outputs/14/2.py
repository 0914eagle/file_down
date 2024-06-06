
import re
import string

def count_syllables(word):
    word = word.lower()
    if re.search('[aeiouy]$', word) is None:
        word = word[:-1]
    if re.search('^es$', word[-2:]):
        word = word[:-2]
    if re.search('^[^aeiouy]?qu[^aeiouy]', word):
        word = re.sub('qu', '', word, 1)
    return len(re.findall('[aeiouy]+', word))

line = input()

words = re.findall('[a-z]+', line)

num_syllables = 0

for word in words:
    num_syllables += count_syllables(word)
    if num_syllables >= 5:
        break

if num_syllables != 5:
    print(line)
else:
    for i in range(0, len(words)):
        if num_syllables == 7:
            print(' '.join(words[:i]))
            num_syllables = 0
        num_syllables += count_syllables(words[i])
