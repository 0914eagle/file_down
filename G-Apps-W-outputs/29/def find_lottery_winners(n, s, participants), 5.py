
def find_lottery_winners(n, s, participants):
    participants.sort(key=lambda x: x[1])  # Sort participants by their bets
    winners = []
    total_sum = 0
    
    for i in range(n):
        total_sum += participants[i][1]
        
        if total_sum == s:
            for j in range(i+1):
                winners.append(participants[j][0])
            break
    
    return len(winners), winners

# Input
n, s = map(int, input().split())
participants = [input().split() for _ in range(n)]

# Convert bet amounts to integers
participants = [(name, int(bet)) for name, bet in participants]

# Output
num_winners, winners = find_lottery_winners(n, s, participants)
print(num_winners)
for winner in winners:
    print(winner)
