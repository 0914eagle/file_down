
def is_beautiful(w):
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

# Input
w = input()

# Check if w is beautiful
print(is_beautiful(w))
```
