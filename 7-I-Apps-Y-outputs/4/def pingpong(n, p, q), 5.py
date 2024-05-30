
def pingpong(n, p, q):
    if p + q == 0:
        return "paul"
    elif (p + q) % 2 == 0:
        return "opponent"
    else:
        return "paul"

print(pingpong(int(input()), int(input()), int(input())))

