
def coconut_splat(s, n):
    hands = [True] * n
    current_hand = 0

    while sum(hands) > 1:
        for _ in range(s):
            current_hand = (current_hand + 1) % n
            while not hands[current_hand]:
                current_hand = (current_hand + 1) % n

        if hands[current_hand]:
            hands[current_hand] = False

    return hands.index(True) + 1

# Input
s, n = map(int, input().split())

# Output
print(coconut_splat(s, n))
