
def min_keystrokes(dictionary, words):
    keystrokes = {}
    for word in words:
        min_keystroke = float('inf')
        for i in range(len(word)):
            prefix = word[:i+1]
            if prefix in dictionary:
                min_keystroke = min(min_keystroke, len(prefix) + 1 + len(word) - len(prefix))
        keystrokes[word] = min_keystroke
    return keystrokes

# Input processing
n, m = map(int, input().split())
dictionary = set()
for _ in range(n):
    dictionary.add(input().strip())
words = [input().strip() for _ in range(m)]

# Calculate and print minimum keystrokes for each word
result = min_keystrokes(dictionary, words)
for word in words:
    print(result[word])

# Sample Input Processing
n, m = 5, 5
dictionary = {'austria', 'autocorrect', 'program', 'programming', 'computer'}
words = ['autocorrelation', 'programming', 'competition', 'zyx', 'austria']
result = min_keystrokes(dictionary, words)
for word in words:
    print(result[word])
```
