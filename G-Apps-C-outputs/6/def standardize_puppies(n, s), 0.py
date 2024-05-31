
def standardize_puppies(n, s):
    colors_count = {}
    for color in s:
        if color in colors_count:
            colors_count[color] += 1
        else:
            colors_count[color] = 1
    
    if len(colors_count) == 1 or max(colors_count.values()) >= n - 1:
        return "Yes"
    else:
        return "No"

# Input
n = int(input())
s = input()

# Output
print(standardize_puppies(n, s))
