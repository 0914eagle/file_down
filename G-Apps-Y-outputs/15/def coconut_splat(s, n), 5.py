
def coconut_splat(s, n):
    remaining_players = list(range(1, n + 1))
    current_index = 0

    while len(remaining_players) > 1:
        syllables = s % len(remaining_players)
        current_index = (current_index + syllables - 1) % len(remaining_players)
        remaining_players.pop(current_index)

    return remaining_players[0]

# Input
s, n = map(int, input().split())

# Output
print(coconut_splat(s, n))
