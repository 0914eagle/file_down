
def determine_order(names):
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

# Call the function and print the output
print(determine_order(names))
