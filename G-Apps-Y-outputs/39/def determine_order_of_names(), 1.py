
def determine_order_of_names():
    n = int(input())
    names = [input() for _ in range(n)]

    increasing = sorted(names)
    decreasing = sorted(names, reverse=True)

    if names == increasing:
        return "INCREASING"
    elif names == decreasing:
        return "DECREASING"
    else:
        return "NEITHER"

print(determine_order_of_names())
