
def determine_lottery_winners(n, s, participants):
    participants.sort(key=lambda x: x[1], reverse=True)
    winners = []

    total_sum = 0
    for i in range(n):
        total_sum += participants[i][1]
        if total_sum == s:
            for j in range(i + 1):
                winners.append(participants[j][0])
            break

    return len(winners), winners

# Input parsing
n, s = map(int, input().split())
participants = []
for _ in range(n):
    name, bet = input().split()
    participants.append((name, int(bet)))

# Determine lottery winners
num_winners, winners = determine_lottery_winners(n, s, participants)

# Output winners
print(num_winners)
for winner in winners:
    print(winner)
