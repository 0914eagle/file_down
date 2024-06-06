
from collections import Counter

def main():
    words = ["be", "our", "rum", "will", "dead", "hook", "ship", "blood", "sable", "avenge", "parrot", "captain"]
    text = input()
    text = text.split()
    for word in words:
        for i in range(len(text)):
            if Counter(word) == Counter(text[i]):
                text[i] = word
    for i in text:
        if i not in words:
            print("Impossible")
            break
    else:
        print(' '.join(text))

if __name__ == "__main__":
    main()
