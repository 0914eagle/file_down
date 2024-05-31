
def check_order(names):
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
names = []
for _ in range(n):
    names.append(input().strip())

# Check order
result = check_order(names)
print(result)
