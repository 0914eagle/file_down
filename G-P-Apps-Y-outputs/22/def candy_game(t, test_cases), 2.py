
def candy_game(t, test_cases):
    results = []
    
    for _ in range(t):
        n = test_cases[_][0]
        candies = test_cases[_][1]
        
        moves = 0
        alice_total = 0
        bob_total = 0
        left = 0
        right = n - 1
        alice_last = 0
        bob_last = 0
        
        while left <= right:
            move_total = 0
            
            if moves % 2 == 0: # Alice's move
                while left <= right and move_total <= bob_last:
                    move_total += candies[left]
                    left += 1
                alice_total += move_total
                alice_last = move_total
            else: # Bob's move
                while left <= right and move_total <= alice_last:
                    move_total += candies[right]
                    right -= 1
                bob_total += move_total
                bob_last = move_total
            
            moves += 1
        
        results.append((moves, alice_total, bob_total))
    
    return results

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    test_cases.append((n, candies))

# Solve and Output
results = candy_game(t, test_cases)
for result in results:
    print(" ".join(map(str, result)))
```
