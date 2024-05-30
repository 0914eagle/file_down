
import sys

def rhyme(word, endings):
    for ending in endings:
        if word.endswith(ending):
            return ending
    return None

def rhyming_slang(word, endings, phrases):
    for phrase in phrases:
        words = phrase.split()
        if len(words) == 2:
            if rhyme(words[0], endings) == rhyme(words[1], endings):
                print("YES")
            else:
                print("NO")
        elif len(words) == 3:
            if rhyme(words[0], endings) == rhyme(words[2], endings):
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    word = input()
    endings = []
    for _ in range(int(input())):
        endings.append(input().split())
    phrases = []
    for _ in range(int(input())):
        phrases.append(input())
    rhyming_slang(word, endings, phrases)

