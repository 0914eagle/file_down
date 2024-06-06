
# 解题思路
# 1. 首先将字符串分割成单词
# 2. 然后将单词进行排列组合
# 3. 最后判断是否在字典中

from itertools import permutations

s = input()
n = int(input())
words = []
for i in range(n):
    words.append(input())

# 字符串分割成单词
word_list = []
word = ''
for i in range(len(s)):
    if s[i] != ' ':
        word += s[i]
    else:
        word_list.append(word)
        word = ''
word_list.append(word)

# 单词排列组合
word_list_per = []
for word in word_list:
    word_list_per.append(list(permutations(word)))

# 排列组合后单词的排列组合
word_list_per_per = list(permutations(word_list_per))

# 判断是否在字典中
for word_list_per in word_list_per_per:
    sentence = ''
    for word in word_list_per:
        sentence += ''.join(word) + ' '
    sentence = sentence.strip()
    if sentence in words:
        print(sentence)
        break
else:
    print('impossible')
