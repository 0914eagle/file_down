
def find_lottery_winners(n, s, participants):
    participants.sort(key=lambda x: x[1])  # Sort participants by their bets
    winners = []
    
    for i in range(n):
        total_bet = participants[i][1]
        possible_winners = [participants[i][0]]
        
        for j in range(i+1, n):
            if total_bet + participants[j][1] == s:
                possible_winners.append(participants[j][0])
        
        if len(possible_winners) > 1:  # If there is more than one winner group
            winners.extend(possible_winners)
            break
    
    return winners

# Input
n, s = map(int, input().split())
participants = []

for _ in range(n):
    name, bet = input().split()
    participants.append((name, int(bet)))

# Output
winners = find_lottery_winners(n, s, participants)
print(len(winners))
for winner in winners:
    print(winner)
