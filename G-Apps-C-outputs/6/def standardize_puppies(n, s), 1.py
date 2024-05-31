
def standardize_puppies(n, s):
    colors = {}
    for color in s:
        if color in colors:
            colors[color] += 1
        else:
            colors[color] = 1
    
    max_count = max(colors.values())
    
    if max_count == n or max_count == n - 1:
        return "Yes"
    else:
        return "No"

# Input
n = int(input())
s = input()

# Output
print(standardize_puppies(n, s))
