
def standardize_puppies(n, s):
    colors_count = {}
    for color in s:
        if color in colors_count:
            colors_count[color] += 1
        else:
            colors_count[color] = 1
    
    max_count = max(colors_count.values())
    
    if max_count == n or max_count >= n - 1:
        print("Yes")
    else:
        print("No")

# Reading input
n = int(input())
s = input().strip()

# Calling the function with input values
standardize_puppies(n, s)
