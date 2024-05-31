
def determine_lottery_winners(n, s, participants):
    winners = []
    highest_bid = 0
    
    for name, bid in participants:
        if bid >= 2 * highest_bid:
            winners.append(name)
            highest_bid = bid
    
    winning_sum = sum(bid for name, bid in participants if name in winners)
    
    if winning_sum == s:
        return len(winners), winners
    else:
        return 0, []

# Input parsing
n, s = map(int, input().split())
participants = [input().split() for _ in range(n)]

# Call the function and print the output
num_winners, winners = determine_lottery_winners(n, s, participants)
print(num_winners)
for winner in winners:
    print(winner)
