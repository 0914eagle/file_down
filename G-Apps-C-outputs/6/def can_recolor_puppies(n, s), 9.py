
def can_recolor_puppies(n, s):
    color_count = {}
    
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    
    max_count = max(color_count.values())
    
    if max_count == n or (n - max_count) >= 2:
        return "Yes"
    else:
        return "No"

# Read input
n = int(input())
s = input()

# Call the function and print the output
print(can_recolor_puppies(n, s))
