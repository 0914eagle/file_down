
def coconut_splat(s, n):
    players = list(range(1, n+1))
    current_player = 0

    while len(players) > 1:
        current_player = (current_player + s - 1) % len(players)
        action = players[current_player]

        if action % 2 == 0:
            players = players[:current_player] + players[current_player+1:]
        else:
            players[current_player] += 1

    return players[0]

# Read input values
s, n = map(int, input().split())

# Call the function and print the result
print(coconut_splat(s, n))
