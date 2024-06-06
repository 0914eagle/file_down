
def un_shuffle(text):
    shuffled = ''.join(reversed(text))
    i = int(len(shuffled)/2)
    first = shuffled[:i]
    last = shuffled[i:]
    return first + last

def check_words(words, shuffle):
    
    for word in words:
        if word == shuffle:
            return word
    return ""

def main():
    text = input()
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        words.append(word)
    words = list(set(words))
    words.sort(key=len)
    words.sort()
    if len(words) == 0:
        print("impossible")
        return
    possible = []
    shuffle = un_shuffle(text)
    if len(words) == 1:
        print("ambiguous")
        return
    for word in words:
        if check_words(words, shuffle) == word:
            possible.append(word)
    if len(possible) == 0:
        print("impossible")
    elif len(possible) == 1:
        print(possible[0])
    else:
        print("ambiguous")

main()
