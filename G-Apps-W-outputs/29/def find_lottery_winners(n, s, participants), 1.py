
def find_lottery_winners(n, s, participants):
    participants.sort(key=lambda x: x[1], reverse=True)
    
    winning_participants = []
    total_bet_sum = 0
    for name, bet in participants:
        if bet >= total_bet_sum + s:
            winning_participants.append(name)
        total_bet_sum += bet
    
    return len(winning_participants), winning_participants

# Input processing
n, s = map(int, input().split())
participants = []
for _ in range(n):
    name, bet = input().split()
    participants.append((name, int(bet)))

# Find lottery winners
num_winners, winners = find_lottery_winners(n, s, participants)

# Output
print(num_winners)
for winner in winners:
    print(winner)
