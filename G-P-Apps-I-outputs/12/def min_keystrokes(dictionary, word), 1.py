
def min_keystrokes(dictionary, word):
    i = 0
    j = 0
    keystrokes = 0
    while i < len(word):
        if j < len(dictionary) and word[i] == dictionary[j]:
            i += 1
            j += 1
        else:
            keystrokes += 1
            i += 1
    return keystrokes + len(word) - j

n, m = map(int, input().split())
dictionary = [input().strip() for _ in range(n)]

for _ in range(m):
    word = input().strip()
    min_keystrokes = min_keystrokes(dictionary, word)
    print(min_keystrokes)
```
