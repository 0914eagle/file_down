
def ping_pong(n, p, q):
    if p+q == n:
        return 'opponent'
    else:
        return 'paul'

print(ping_pong(int(input()), int(input()), int(input())))

