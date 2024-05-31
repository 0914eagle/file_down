
def coconut_splat(s, n):
    hands = [1] * n
    current_player = 0

    while sum(hands) > 1:
        for i in range(s - 1):
            current_player = (current_player + 1) % n
            while hands[current_player] == 0:
                current_player = (current_player + 1) % n

        if hands[current_player] == 1:
            hands[current_player] = 0
        else:
            hands[current_player] = 1

    return hands.index(1) + 1

# Input
s, n = map(int, input().split())

# Output
print(coconut_splat(s, n))
