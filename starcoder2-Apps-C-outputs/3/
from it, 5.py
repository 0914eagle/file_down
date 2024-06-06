
from itertools import permutations

s = input()
n = int(input())
words = []
for i in range(n):
    words.append(input())

for word in permutations(words):
    res = []
    for i in range(len(s)):
        if i == 0:
            res.append(s[i])
        elif i == len(s) - 1:
            res.append(s[i])
        else:
            res.append(word[int(s[i]) - 1])
    if ''.join(res) in words:
        print(' '.join(res))
        break
else:
    print('impossible')
