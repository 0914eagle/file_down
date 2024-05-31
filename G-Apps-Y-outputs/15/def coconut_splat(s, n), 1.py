
def coconut_splat(s, n):
    players = list(range(1, n+1))
    current_index = 0

    while len(players) > 1:
        for _ in range(s-1):
            current_index = (current_index + 1) % len(players)
        action = players[current_index]

        if action % 2 == 1:  # Split into two fists
            players.insert(current_index + 1, players[current_index])
            current_index += 1
        elif action % 3 == 0:  # Turn hand palm down
            current_index = (current_index + 1) % len(players)
        elif action % 5 == 0:  # Put hand behind back
            players.pop(current_index)
            if current_index == len(players):
                current_index = 0

    return players[0]

# Input
s, n = map(int, input().split())

# Output
print(coconut_splat(s, n))
