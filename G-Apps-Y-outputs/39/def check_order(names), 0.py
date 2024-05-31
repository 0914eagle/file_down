
def check_order(names):
    increasing = sorted(names)
    decreasing = sorted(names, reverse=True)
    
    if names == increasing:
        return "INCREASING"
    elif names == decreasing:
        return "DECREASING"
    else:
        return "NEITHER"

N = int(input())
names = [input() for _ in range(N)]

print(check_order(names))
