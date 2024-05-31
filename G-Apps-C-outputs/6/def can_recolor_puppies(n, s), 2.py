
def can_recolor_puppies(n, s):
    colors = set(s)
    for color in colors:
        if s.count(color) >= 2:
            return "Yes"
    return "No"

# Input
n = int(input())
s = input().strip()

# Output
print(can_recolor_puppies(n, s))
