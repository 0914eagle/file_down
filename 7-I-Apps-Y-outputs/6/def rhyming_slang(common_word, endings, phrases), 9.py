
import re

def rhyming_slang(common_word, endings, phrases):
    endings = [set(e.split()) for e in endings]
    for p in phrases:
        words = p.split()
        if len(words) == 2:
            if words[1] in endings[0]:
                yield 'YES'
            else:
                yield 'NO'
        elif len(words) == 3:
            if words[1] in endings[0] and words[2] in endings[1]:
                yield 'YES'
            else:
                yield 'NO'

common_word = input()
endings = [input().split() for _ in range(int(input()))]
phrases = [input() for _ in range(int(input()))]
for p in rhyming_slang(common_word, endings, phrases):
    print(p)

