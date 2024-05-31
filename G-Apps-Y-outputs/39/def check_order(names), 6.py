
def check_order(names):
    increasing = sorted(names)
    decreasing = sorted(names, reverse=True)
    
    if names == increasing:
        return "INCREASING"
    elif names == decreasing:
        return "DECREASING"
    else:
        return "NEITHER"

n = int(input())
names = []
for _ in range(n):
    name = input().strip()
    names.append(name)

result = check_order(names)
print(result)
