
def candy_game(t, test_cases):
    def play_game(n, candies):
        moves = 0
        alice_total = 0
        bob_total = 0
        alice_turn = True

        left, right = 0, n - 1

        while left <= right:
            move_total = 0

            if alice_turn:
                move_total += candies[left]
                alice_total += move_total
                left += 1
            else:
                move_total += candies[right]
                bob_total += move_total
                right -= 1

            moves += 1
            alice_turn = not alice_turn

            while left <= right and move_total <= bob_total + alice_turn * candies[left]:
                if alice_turn:
                    move_total += candies[left]
                    alice_total += candies[left]
                    left += 1
                else:
                    move_total += candies[right]
                    bob_total += candies[right]
                    right -= 1

        return moves, alice_total, bob_total

    for i in range(t):
        n = test_cases[i][0]
        candies = test_cases[i][1]
        moves, alice_total, bob_total = play_game(n, candies)
        print(moves, alice_total, bob_total)

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    test_cases.append((n, candies))

candy_game(t, test_cases)
