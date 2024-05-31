
def standardize_puppies(n, s):
    color_count = {}
    
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    
    max_count = max(color_count.values())
    
    if max_count == n or max_count > (n + 1) // 2:
        return "No"
    else:
        return "Yes"

# Input
n = int(input())
s = input()

# Output
print(standardize_puppies(n, s))
