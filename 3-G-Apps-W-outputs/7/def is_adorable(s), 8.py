
def is_adorable(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    for count in counts.values():
        if count >= 2:
            return "Yes"
    
    return "No"

# Input
s = input().strip()

# Output
print(is_adorable(s))
