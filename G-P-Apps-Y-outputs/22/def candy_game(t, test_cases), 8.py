
def candy_game(t, test_cases):
    for n, candies in test_cases:
        moves = 0
        alice_total = 0
        bob_total = 0
        alice_eating = True
        
        left = 0
        right = n - 1
        
        while left <= right:
            current_sum = 0
            if alice_eating:
                current_sum += candies[left]
                alice_total += candies[left]
                left += 1
                moves += 1
                alice_eating = False
            else:
                current_sum += candies[right]
                bob_total += candies[right]
                right -= 1
                moves += 1
                alice_eating = True
            
            while left <= right and current_sum <= bob_total:
                if alice_eating:
                    current_sum += candies[left]
                    alice_total += candies[left]
                    left += 1
                    moves += 1
                    alice_eating = False
                else:
                    current_sum += candies[right]
                    bob_total += candies[right]
                    right -= 1
                    moves += 1
                    alice_eating = True
        
        print(moves, alice_total, bob_total)

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    test_cases.append((n, candies))

# Output
candy_game(t, test_cases)
```
