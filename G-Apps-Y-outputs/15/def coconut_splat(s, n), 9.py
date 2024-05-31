
def coconut_splat(s, n):
    hands = [True] * n  # Initialize all players' hands as folded
    
    current_player = 0  # Start with player 1
    while sum(hands) > 1:
        for _ in range(s):
            while not hands[current_player]:  # Skip players with hands behind their back
                current_player = (current_player + 1) % n
            current_player = (current_player + 1) % n  # Move to the next player
        
        while not hands[current_player]:  # Skip players with hands behind their back
            current_player = (current_player + 1) % n
        
        if hands[current_player]:  # Check if the player still has their hands folded
            hands[current_player] = False
        else:  # If the player's hands are already split or palm down, move to the next hand
            current_player = (current_player + 1) % n
    
    for i, hand in enumerate(hands):
        if hand:
            return i + 1

# Input
s, n = map(int, input().split())
# Output
print(coconut_splat(s, n))
