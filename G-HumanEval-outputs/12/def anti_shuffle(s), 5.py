
def anti_shuffle(s):
    words = s.split()
    ordered_words = []
    
    for word in words:
        ordered_word = ''.join(sorted(word))
        ordered_words.append(ordered_word)
    
    return ' '.join(ordered_words)

# Test cases
print(anti_shuffle('Hi'))  # Output: 'Hi'
print(anti_shuffle('hello'))  # Output: 'ehllo'
print(anti_shuffle('Hello World!!!'))  # Output: 'Hello !!!Wdlor'
```
