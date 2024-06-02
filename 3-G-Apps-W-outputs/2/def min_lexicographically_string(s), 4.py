
def min_lexicographically_string(s):
    n = len(s)
    s = list(s)
    
    # Count the occurrences of each character
    count = [0, 0, 0]
    for char in s:
        count[int(char)] += 1
    
    # Update the string based on the counts
    idx = 0
    for i in range(count[0]):
        s[idx] = '0'
        idx += 1
    for i in range(count[1]):
        s[idx] = '1'
        idx += 1
    for i in range(count[2]):
        s[idx] = '2'
        idx += 1
    
    return ''.join(s)

# Read input
s = input().strip()

# Output the minimum lexicographically string
print(min_lexicographically_string(s))
