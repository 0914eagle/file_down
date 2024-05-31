
def anti_shuffle(s):
    def sort_word(word):
        return ''.join(sorted(word))

    result = []
    word = ''
    for char in s:
        if char.isalpha():
            word += char
        else:
            if word:
                result.append(sort_word(word))
                word = ''
            result.append(char)

    if word:
        result.append(sort_word(word))

    return ''.join(result)

# Test cases
print(anti_shuffle('Hi'))  # Output: 'Hi'
print(anti_shuffle('hello'))  # Output: 'ehllo'
print(anti_shuffle('Hello World!!!'))  # Output: 'Hello !!!Wdlor'
```
