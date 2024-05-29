
def is_beautiful_string(w):
    letter_counts = {}
    for letter in w:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    for count in letter_counts.values():
        if count % 2 != 0:
            return "No"
    
    return "Yes"

w = input().strip()
print(is_beautiful_string(w))
```
