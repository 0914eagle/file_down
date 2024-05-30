
def ping_pong(N, P, Q):
    if P + Q == 0:
        return "paul"
    elif (P + Q) % N == 0:
        return "opponent"
    else:
        return "paul"

N, P, Q = map(int, input().split())
print(ping_pong(N, P, Q))

