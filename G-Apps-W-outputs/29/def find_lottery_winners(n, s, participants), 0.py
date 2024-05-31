
def find_lottery_winners(n, s, participants):
    participants.sort(key=lambda x: x[1], reverse=True)
    
    winners = []
    total_bet = 0
    for name, bet in participants:
        if total_bet + bet <= s:
            winners.append(name)
            total_bet += bet
    
    return len(winners), winners

# Input processing
n, s = map(int, input().split())
participants = []
for _ in range(n):
    name, bet = input().split()
    participants.append((name, int(bet)))

# Find lottery winners
num_winners, winners = find_lottery_winners(n, s, participants)

# Output results
print(num_winners)
for winner in winners:
    print(winner)
