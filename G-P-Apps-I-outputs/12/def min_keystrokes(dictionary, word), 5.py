
def min_keystrokes(dictionary, word):
    min_keystrokes = 0
    for char in word:
        if dictionary.startswith(word[:len(dictionary)+1]):
            min_keystrokes += 1
        else:
            min_keystrokes += 1 + len(word) - len(dictionary)
            break
    return min_keystrokes

n, m = map(int, input().split())
dict_words = [input() for _ in range(n)]

for _ in range(m):
    word = input()
    min_strokes = min_keystrokes(next((w for w in dict_words if w.startswith(word)), word), word)
    print(min_strokes)
```
