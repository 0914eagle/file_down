
def coconut_splat(s, n):
    players = list(range(1, n+1))
    idx = 0

    while len(players) > 1:
        touches = s % len(players)
        idx = (idx + touches - 1) % len(players)
        
        if players[idx] == 1:
            players.append(players.pop(idx))
        else:
            players.pop(idx)

    return players[0]

# Input
s, n = map(int, input().split())

# Output
print(coconut_splat(s, n))
