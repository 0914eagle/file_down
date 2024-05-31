
def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        odd_letters = [char for char in txt if char.islower() and ord(char) % 2 != 0]
        return len(odd_letters)

# Test cases
print(split_words("Hello world!"))  # ➞ ["Hello", "world!"]
print(split_words("Hello,world!"))  # ➞ ["Hello", "world!"]
print(split_words("abcdef"))  # ➞ 3
```
