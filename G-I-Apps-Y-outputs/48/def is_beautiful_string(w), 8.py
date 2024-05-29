
def is_beautiful_string(w):
    char_count = {}
    for char in w:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for count in char_count.values():
        if count % 2 != 0:
            return "No"
    
    return "Yes"

w = input()
print(is_beautiful_string(w))
```
