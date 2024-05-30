
def min_keystrokes(dictionary, words):
    keystrokes = []
    
    for word in words:
        min_keystroke = float('inf')
        
        for i in range(len(word)):
            prefix = word[:i+1]
            
            for dict_word in dictionary:
                if dict_word.startswith(prefix):
                    completion_keystrokes = len(dict_word) - len(prefix)
                    min_keystroke = min(min_keystroke, len(prefix) + 1 + completion_keystrokes)
                    break
        
        keystrokes.append(min_keystroke)
    
    return keystrokes

n, m = map(int, input().split())
dictionary = [input() for _ in range(n)]
words = [input() for _ in range(m)]

result = min_keystrokes(dictionary, words)
for res in result:
    print(res)
```
