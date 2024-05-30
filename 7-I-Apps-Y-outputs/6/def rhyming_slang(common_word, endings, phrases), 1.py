
import sys

def rhyming_slang(common_word, endings, phrases):
    # Write your code here
    return []

if __name__ == "__main__":
    common_word = input()
    endings_count = int(input())
    endings = []
    for i in range(endings_count):
        endings.append(input().split())
    phrases_count = int(input())
    phrases = []
    for i in range(phrases_count):
        phrases.append(input())
    print('\n'.join(rhyming_slang(common_word, endings, phrases)))

