
def coconut_splat(s, n):
    players = list(range(1, n + 1))
    hand_status = [0] * n
    current_player = 0
    
    while len(players) > 1:
        for syllable in range(s):
            current_player = (current_player + 1) % len(players)
            hand = hand_status[current_player]
            
            if hand == 0:
                hand_status[current_player] = 1
            elif hand == 1:
                hand_status[current_player] = 2
            elif hand == 2:
                hand_status[current_player] = 3
                players.remove(players[current_player])
                if current_player == len(players):
                    current_player = 0
            elif hand == 3:
                hand_status[current_player] = 0
                
    return players[0]

# Input
s, n = map(int, input().split())

# Output
print(coconut_splat(s, n))
