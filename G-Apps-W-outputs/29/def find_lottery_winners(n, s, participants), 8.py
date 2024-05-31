
def find_lottery_winners(n, s, participants):
    participants.sort(key=lambda x: x[1])  # Sort participants by their bets
    winners = []
    total_bet = 0

    for participant in participants:
        name, bet = participant
        if total_bet + bet <= s:
            total_bet += bet
            winners.append(name)

    return len(winners), winners

# Input parsing
n, s = map(int, input().split())
participants = []
for _ in range(n):
    name, bet = input().split()
    participants.append((name, int(bet)))

# Find lottery winners
num_winners, winners = find_lottery_winners(n, s, participants)

# Output the results
print(num_winners)
for winner in winners:
    print(winner)
