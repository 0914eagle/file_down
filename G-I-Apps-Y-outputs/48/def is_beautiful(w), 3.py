
def is_beautiful(w):
    letter_count = {}
    for letter in w:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    for count in letter_count.values():
        if count % 2 != 0:
            return "No"
    
    return "Yes"

w = input().strip()
print(is_beautiful(w))
```
