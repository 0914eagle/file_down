
def anti_shuffle(s):
    def sort_word(word):
        return ''.join(sorted(word))

    words = s.split()
    sorted_words = [sort_word(word) for word in words]

    output = ''
    for i, word in enumerate(sorted_words):
        output += word
        if i < len(sorted_words) - 1:
            output += ' '

    return output

# Test cases
print(anti_shuffle('Hi'))  # Output: Hi
print(anti_shuffle('hello'))  # Output: ehllo
print(anti_shuffle('Hello World!!!'))  # Output: Hello !!!Wdlor
```
