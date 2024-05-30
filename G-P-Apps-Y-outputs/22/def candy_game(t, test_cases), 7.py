
def candy_game(t, test_cases):
    result = []
    
    for i in range(t):
        n = test_cases[i][0]
        candies = test_cases[i][1]

        alice_total = 0
        bob_total = 0
        alice_moves = 0
        bob_moves = 0
        alice_turn = True

        left = 0
        right = n - 1

        while left <= right:
            if alice_turn:
                alice_moves += 1
                alice_sum = 0
                while left <= right and alice_sum <= bob_total:
                    alice_sum += candies[left]
                    alice_total += candies[left]
                    left += 1
                alice_turn = False
            else:
                bob_moves += 1
                bob_sum = 0
                while right >= left and bob_sum <= alice_total:
                    bob_sum += candies[right]
                    bob_total += candies[right]
                    right -= 1
                alice_turn = True

        result.append((alice_moves + bob_moves, alice_total, bob_total))

    return result


t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    test_cases.append((n, candies))

output = candy_game(t, test_cases)

for o in output:
    print(*o)
```
