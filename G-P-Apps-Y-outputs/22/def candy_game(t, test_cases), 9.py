
def candy_game(t, test_cases):
    for i in range(t):
        n = test_cases[i][0]
        candies = test_cases[i][1]

        moves = 1
        alice_total = candies[0]
        bob_total = 0
        alice_eaten = candies[0]
        bob_eaten = 0

        left = 1
        right = n - 1

        while left <= right:
            if moves % 2 == 1:  # Alice's turn
                total = 0
                while total <= bob_total and left <= right:
                    total += candies[left]
                    alice_eaten += candies[left]
                    left += 1
                alice_total += total
            else:  # Bob's turn
                total = 0
                while total <= alice_total and left <= right:
                    total += candies[right]
                    bob_eaten += candies[right]
                    right -= 1
                bob_total += total

            moves += 1

        print(moves - 1, alice_total, bob_total)

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    test_cases.append((n, candies))

# Call function with input
candy_game(t, test_cases)
```
