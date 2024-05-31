
def expected_score(n, c, deck):
    deck.sort()
    max_score = deck[c]
    sum_scores = sum(deck[:c]) + max_score * (n - c)
    total_permutations = 1 << n

    dp = [0.0] * (1 << n)
    for mask in range(1, total_permutations):
        max_seen = -1
        score_sum = 0
        num_cards_seen = 0
        for i in range(n):
            if mask & (1 << i):
                num_cards_seen += 1
                if deck[i] > max_seen:
                    max_seen = deck[i]
                    score_sum = max(dp[mask ^ (1 << i)], score_sum)

        dp[mask] = score_sum + max_score

    expected = sum(dp) / total_permutations
    return expected

# Read input
n, c = map(int, input().split())
deck = list(map(int, input().split()))

# Calculate and print expected score
print("{:.6f}".format(expected_score(n, c, deck)))
