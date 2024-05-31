
def determine_lottery_winners(n, s, participants):
    participants.sort(key=lambda x: x[1])  # Sort participants by their bets
    winning_participants = []
    
    for i in range(n):
        total_bet = 0
        current_winners = []
        
        for j in range(i, n):
            total_bet += participants[j][1]
            current_winners.append(participants[j][0])
            
            if total_bet == s:
                winning_participants.extend(current_winners)
                break
            elif total_bet > s:
                break
    
    winning_participants.sort()  # Sort the names of winning participants
    
    print(len(winning_participants))
    for participant in winning_participants:
        print(participant)

# Read input
n, s = map(int, input().split())
participants = []
for _ in range(n):
    name, bet = input().split()
    participants.append((name, int(bet)))

# Call the function with the input data
determine_lottery_winners(n, s, participants)
