
def find_smallest_missing_letter(s):
    char_set = set()
    for char in s:
        char_set.add(char)
    
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in char_set:
            return char
    
    return None

s = input()
result = find_smallest_missing_letter(s)
print(result)

