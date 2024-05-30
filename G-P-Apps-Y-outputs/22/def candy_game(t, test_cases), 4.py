
def candy_game(t, test_cases):
    for case in test_cases:
        n = case[0]
        candies = case[1]

        moves = 0
        alice_total = 0
        bob_total = 0

        left = 0
        right = n - 1
        alice_sum = 0
        bob_sum = 0

        while left <= right:
            if moves % 2 == 0:  # Alice's turn
                alice_sum = 0
                while alice_sum <= bob_sum and left <= right:
                    alice_sum += candies[left]
                    alice_total += candies[left]
                    left += 1
                bob_sum = alice_sum
            else:  # Bob's turn
                bob_sum = 0
                while bob_sum <= alice_sum and left <= right:
                    bob_sum += candies[right]
                    bob_total += candies[right]
                    right -= 1
                alice_sum = bob_sum

            moves += 1

        print(moves, alice_total, bob_total)

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    test_cases.append((n, candies))

candy_game(t, test_cases)
```
