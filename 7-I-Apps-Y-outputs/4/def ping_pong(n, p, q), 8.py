
def ping_pong(n, p, q):
    if p+q < n:
        return "paul"
    else:
        return "opponent"

print(ping_pong(int(input()), int(input()), int(input())))

