
def determine_lottery_winners(n, s, participants):
    participants.sort(key=lambda x: x[1], reverse=True)  # Sort participants by their bets in descending order
    winning_participants = []
    
    for i in range(n):
        current_bet = participants[i][1]
        total_bet = sum([p[1] for p in participants[:i]])
        
        if current_bet >= 2 * total_bet and total_bet + current_bet == s:
            winning_participants.append(participants[i][0])
    
    print(len(winning_participants))
    for participant in winning_participants:
        print(participant)

# Input processing
n, s = map(int, input().split())
participants = []
for _ in range(n):
    name, bet = input().split()
    participants.append((name, int(bet)))

# Call the function with the input data
determine_lottery_winners(n, s, participants)
