
def ping_pong(N, P, Q):
    if P + Q == 0:
        return 'paul'
    if (P + Q) % N == 0:
        return 'opponent'
    return 'paul'

N, P, Q = map(int, input().split())
print(ping_pong(N, P, Q))

