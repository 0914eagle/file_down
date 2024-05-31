
def determine_order_of_names():
    N = int(input())
    names = []
    for i in range(N):
        name = input().strip()
        names.append(name)

    increasing = sorted(names) == names
    decreasing = sorted(names, reverse=True) == names

    if increasing:
        print("INCREASING")
    elif decreasing:
        print("DECREASING")
    else:
        print("NEITHER")

determine_order_of_names()
