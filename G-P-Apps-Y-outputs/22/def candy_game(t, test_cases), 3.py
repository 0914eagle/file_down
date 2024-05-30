
def candy_game(t, test_cases):
    results = []
    for test in test_cases:
        n = test[0]
        candies = test[1]
        moves = 0
        alice_total = 0
        bob_total = 0
        alice_turn = True

        left = 0
        right = n - 1

        while left <= right:
            move_total = 0
            if alice_turn:
                move_total += candies[left]
                alice_total += candies[left]
                left += 1
                alice_turn = False
            else:
                move_total += candies[right]
                bob_total += candies[right]
                right -= 1
                alice_turn = True

            while left <= right and move_total <= bob_total:
                if alice_turn:
                    move_total += candies[left]
                    alice_total += candies[left]
                    left += 1
                    alice_turn = False
                else:
                    move_total += candies[right]
                    bob_total += candies[right]
                    right -= 1
                    alice_turn = True

            moves += 1

        results.append((moves, alice_total, bob_total))

    return results

test_cases = [
    (11, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),
    (1, [1000]),
    (3, [1, 1, 1]),
    (13, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
    (2, [2, 1]),
    (6, [1, 1, 1, 1, 1, 1]),
    (7, [1, 1, 1, 1, 1, 1, 1])
]

results = candy_game(7, test_cases)
for result in results:
    print(result[0], result[1], result[2])
```
