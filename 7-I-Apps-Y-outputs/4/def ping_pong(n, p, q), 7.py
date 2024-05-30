
def ping_pong(n, p, q):
    if p + q < n:
        return 'paul'
    else:
        return 'opponent'

n, p, q = map(int, input().split())
print(ping_pong(n, p, q))

