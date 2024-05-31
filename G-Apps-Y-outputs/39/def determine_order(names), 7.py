
def determine_order(names):
    increasing = sorted(names) == names
    decreasing = sorted(names, reverse=True) == names
    if increasing:
        return "INCREASING"
    elif decreasing:
        return "DECREASING"
    else:
        return "NEITHER"

# Input processing
N = int(input())
names = [input().strip() for _ in range(N)]

# Check the order
result = determine_order(names)
print(result)
