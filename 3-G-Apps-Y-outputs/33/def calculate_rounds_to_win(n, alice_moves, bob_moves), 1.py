
def calculate_rounds_to_win(n, alice_moves, bob_moves):
    min_wins = max(0, alice_moves[0] - bob_moves[1]) + max(0, alice_moves[1] - bob_moves[2]) + max(0, alice_moves[2] - bob_moves[0])
    max_wins = min(alice_moves[0], bob_moves[2]) + min(alice_moves[1], bob_moves[0]) + min(alice_moves[2], bob_moves[1])
    
    return min_wins, max_wins

# Input
n = int(input())
alice_moves = list(map(int, input().split()))
bob_moves = list(map(int, input().split()))

# Calculate and output results
min_wins, max_wins = calculate_rounds_to_win(n, alice_moves, bob_moves)
print(min_wins, max_wins)
