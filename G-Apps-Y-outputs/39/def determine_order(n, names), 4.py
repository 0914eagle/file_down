
def determine_order(n, names):
    increasing = sorted(names)
    decreasing = sorted(names, reverse=True)
    
    if names == increasing:
        return "INCREASING"
    elif names == decreasing:
        return "DECREASING"
    else:
        return "NEITHER"

# Read input
n = int(input())
names = [input().strip() for _ in range(n)]

# Output result
print(determine_order(n, names))
