
def ping_pong(N, P, Q):
    if (P + Q) % 2 == 0:
        return "opponent"
    else:
        return "paul"

N, P, Q = map(int, input().split())
print(ping_pong(N, P, Q))

