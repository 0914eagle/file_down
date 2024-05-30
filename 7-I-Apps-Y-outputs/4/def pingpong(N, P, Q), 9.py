
def pingpong(N, P, Q):
    if P+Q == 0:
        return "paul"
    if (P+Q)%N == 0:
        return "opponent"
    else:
        return "paul"

N, P, Q = map(int, input().split())
print(pingpong(N, P, Q))

