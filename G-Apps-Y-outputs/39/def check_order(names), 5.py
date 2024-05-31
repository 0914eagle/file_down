
def check_order(names):
    increasing = sorted(names) == names
    decreasing = sorted(names, reverse=True) == names

    if increasing:
        return "INCREASING"
    elif decreasing:
        return "DECREASING"
    else:
        return "NEITHER"

# Input processing
n = int(input())
names = []
for _ in range(n):
    names.append(input().strip())

result = check_order(names)
print(result)
