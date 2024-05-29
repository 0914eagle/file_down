
def is_beautiful(w):
    count = {}
    
    for letter in w:
        count[letter] = count.get(letter, 0) + 1
    
    for val in count.values():
        if val % 2 != 0:
            return "No"
    
    return "Yes"

w = input()
print(is_beautiful(w))
```
