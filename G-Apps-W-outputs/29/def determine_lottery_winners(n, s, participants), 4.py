
def determine_lottery_winners(n, s, participants):
    participants.sort(key=lambda x: x[1], reverse=True)
    
    winning_participants = []
    total_bet_sum = 0
    for participant in participants:
        if total_bet_sum + participant[1] <= s:
            total_bet_sum += participant[1]
            winning_participants.append(participant[0])
    
    print(len(winning_participants))
    for participant in winning_participants:
        print(participant)

# Input
n, s = map(int, input().split())
participants = []
for _ in range(n):
    name, bet = input().split()
    participants.append((name, int(bet)))

# Call the function
determine_lottery_winners(n, s, participants)
