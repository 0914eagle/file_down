
def coconut_splat(s, n):
    players = [True] * n  # Initialize all players as active
    current_player = 0  # Start counting from player 1
    remaining_players = n  # Number of players still in the game

    while remaining_players > 1:
        for _ in range(s-1):
            while not players[current_player]:
                current_player = (current_player + 1) % n  # Skip inactive players

            current_player = (current_player + 1) % n  # Move to the next player

        while not players[current_player]:
            current_player = (current_player + 1) % n  # Skip inactive players

        # Perform actions based on the player touched last
        if players[current_player]:
            players[current_player] = False  # Player is out of the game
            remaining_players -= 1

        current_player = (current_player + 1) % n  # Move to the next player

    return players.index(True) + 1  # Return the index of the remaining player

# Input
s, n = map(int, input().split())

# Output
print(coconut_splat(s, n))
