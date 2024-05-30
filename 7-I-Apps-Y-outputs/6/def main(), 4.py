
import sys

def main():
    common_word = input()
    endings = int(input())
    end_lists = []
    for i in range(endings):
        end_lists.append(input().split())
    phrases = int(input())
    for i in range(phrases):
        phrase = input()
        if phrase.count(' ') == 2:
            word1, word2, word3 = phrase.split()
            if word1[-1] in end_lists[0] and word2[-1] in end_lists[0] and word3[-1] in end_lists[1]:
                print('YES')
            else:
                print('NO')
        elif phrase.count(' ') == 1:
            word1, word2 = phrase.split()
            if word1[-1] in end_lists[0] and word2[-1] in end_lists[1]:
                print('YES')
            else:
                print('NO')

if __name__ == '__main__':
    main()

