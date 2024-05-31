
def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = sum(1 for c in txt if c.islower() and ord(c) % 2 == 1)
        return count

# Test cases
print(split_words("Hello world!"))  # ➞ ["Hello", "world!"]
print(split_words("Hello,world!"))  # ➞ ["Hello", "world!"]
print(split_words("abcdef"))  # ➞ 3
