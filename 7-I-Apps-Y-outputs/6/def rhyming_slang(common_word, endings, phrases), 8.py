
import sys

def rhyming_slang(common_word, endings, phrases):
    rhyming_slang_phrases = []
    for phrase in phrases:
        words = phrase.split()
        if len(words) == 2:
            if words[0][-1] == words[1][-1]:
                rhyming_slang_phrases.append("YES")
            else:
                rhyming_slang_phrases.append("NO")
        elif len(words) == 3:
            if words[0][-1] == words[2][-1]:
                if words[1] in endings:
                    rhyming_slang_phrases.append("YES")
                else:
                    rhyming_slang_phrases.append("NO")
            else:
                rhyming_slang_phrases.append("NO")
    return rhyming_slang_phrases

def main():
    common_word = input()
    endings = []
    for _ in range(int(input())):
        endings.append(input().split())
    phrases = []
    for _ in range(int(input())):
        phrases.append(input())
    for phrase in rhyming_slang(common_word, endings, phrases):
        print(phrase)

if __name__ == "__main__":
    main()

