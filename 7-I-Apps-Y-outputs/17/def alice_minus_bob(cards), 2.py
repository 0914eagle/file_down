
def alice_minus_bob(cards):
    # Write your code here
    alice_score = 0
    bob_score = 0
    for i in range(len(cards)):
        if i % 2 == 0:
            alice_score += cards[i]
        else:
            bob_score += cards[i]
    return alice_score - bob_score

