
import re
import sys

s = sys.stdin.readline().strip()
l = re.split('[^a-zA-Z]', s)
l = [x for x in l if x]
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def checkSyllable(word):
    word = word.lower()
    length = len(word)
    if length == 0:
        return 0
    count = 0
    prevChar = ''
    for i in range(0, length):
        if word[i] in vowels:
            if i == length - 1:
                if prevChar != 'e':
                    count += 1
            elif word[i] != 'e' and i < length - 1 and word[i+1] != 'e':
                count += 1
        prevChar = word[i]
    return count

count = 0
for i in range(len(l)):
    count += checkSyllable(l[i])

if count == 5:
    line1 = ''
    line2 = ''
    line3 = ''
    i = 0
    while i < len(l):
        if checkSyllable(l[i]) + checkSyllable(l[i+1]) > 7:
            line1 += l[i] + ' '
            i += 1
        else:
            line1 += l[i] + ' '
            line2 += l[i+1] + ' '
            i += 2
    for i in range(i, len(l)):
        line3 += l[i] + ' '
    print(line1)
    print(line2)
    print(line3)
else:
    print(s)
