


def ping_pong(n, p, q):
    if p+q == n:
        return "opponent"
    else:
        return "paul"


n, p, q = map(int, input().split())
print(ping_pong(n, p, q))

