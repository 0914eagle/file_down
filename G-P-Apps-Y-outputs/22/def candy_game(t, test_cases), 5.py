
def candy_game(t, test_cases):
    res = []
    for case in test_cases:
        n = case[0]
        candies = case[1]

        moves = 0
        alice_total = 0
        bob_total = 0
        alice_eaten = bob_eaten = 0
        alice_turn = True

        left = 0
        right = n - 1

        while left <= right:
            if alice_turn:
                alice_total += candies[left]
                alice_eaten = candies[left]
                left += 1
                while left <= right and bob_eaten <= alice_eaten:
                    bob_total += candies[right]
                    bob_eaten = candies[right]
                    right -= 1
                alice_turn = False
            else:
                bob_total += candies[right]
                bob_eaten = candies[right]
                right -= 1
                while left <= right and alice_eaten <= bob_eaten:
                    alice_total += candies[left]
                    alice_eaten = candies[left]
                    left += 1
                alice_turn = True

            moves += 1

        res.append((moves, alice_total, bob_total))

    return res

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    test_cases.append((n, candies))

# Output
results = candy_game(t, test_cases)
for result in results:
    print(*result)
