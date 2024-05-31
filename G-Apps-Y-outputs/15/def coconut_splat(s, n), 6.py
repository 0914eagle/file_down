
def coconut_splat(s, n):
    players = list(range(1, n+1))
    current_index = 0

    while len(players) > 1:
        current_index = (current_index + s - 1) % len(players)
        action = players[current_index]

        if action in players:
            players.remove(action)
        else:
            players.pop(current_index)

    return players[0]

# Input
s, n = map(int, input().split())

# Output
print(coconut_splat(s, n))
