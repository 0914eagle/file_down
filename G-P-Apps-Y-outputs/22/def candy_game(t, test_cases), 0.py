
def candy_game(t, test_cases):
    for i in range(t):
        n = test_cases[i][0]
        candies = test_cases[i][1]
        
        moves = 0
        alice_total = 0
        bob_total = 0
        alice_eaten = 0
        bob_eaten = 0
        
        left = 0
        right = n - 1
        
        while left <= right:
            if moves % 2 == 0:  # Alice's turn
                alice_eaten = 0
                while left <= right and alice_eaten <= bob_total:
                    alice_eaten += candies[left]
                    alice_total += candies[left]
                    left += 1
                moves += 1
            else:  # Bob's turn
                bob_eaten = 0
                while left <= right and bob_eaten <= alice_total:
                    bob_eaten += candies[right]
                    bob_total += candies[right]
                    right -= 1
                moves += 1
        
        print(moves, alice_total, bob_total)

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    test_cases.append((n, candies))

candy_game(t, test_cases)
```
