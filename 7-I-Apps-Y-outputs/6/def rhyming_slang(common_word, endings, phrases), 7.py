
import re

def rhyming_slang(common_word, endings, phrases):
    # Write your code here
    endings_dict = {}
    for end in endings:
        for end_word in end.split():
            if end_word not in endings_dict:
                endings_dict[end_word] = []
            endings_dict[end_word].append(end)
    for phrase in phrases:
        words = phrase.split()
        if len(words) == 2:
            if words[1] in endings_dict and words[1][-len(common_word):] in endings_dict[words[1]]:
                print('YES')
            else:
                print('NO')
        elif len(words) == 3:
            if words[1] in endings_dict and words[1][-len(common_word):] in endings_dict[words[1]] and words[2] in endings_dict and words[2][-len(common_word):] in endings_dict[words[2]]:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')

if __name__ == '__main__':
    common_word = input()
    endings_num = int(input())
    endings = []
    for _ in range(endings_num):
        endings.append(input())
    phrases_num = int(input())
    phrases = []
    for _ in range(phrases_num):
        phrases.append(input())
    rhyming_slang(common_word, endings, phrases)

