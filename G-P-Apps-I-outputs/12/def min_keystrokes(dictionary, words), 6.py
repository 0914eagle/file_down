
def min_keystrokes(dictionary, words):
    keystrokes = []
    for word in words:
        min_keystroke = len(word)
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            j = 0
            while j < len(dictionary) and j < len(prefix):
                if dictionary[j] == prefix[j]:
                    j += 1
                else:
                    break
            if j == len(prefix):
                min_keystroke = min(min_keystroke, len(word) - j + len(prefix) + 1)
        keystrokes.append(min_keystroke)
    return keystrokes

n, m = map(int, input().split())
dictionary = [input() for _ in range(n)]
words = [input() for _ in range(m)]

results = min_keystrokes(dictionary, words)
for result in results:
    print(result)
```
