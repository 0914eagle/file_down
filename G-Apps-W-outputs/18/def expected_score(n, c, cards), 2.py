
def expected_score(n, c, cards):
    cards.sort()
    max_score = 0
    for i in range(c, n):
        max_score = max(max_score, cards[i])
    
    expected = 0
    for i in range(c):
        expected += cards[i]
    expected += (n - c) * max_score
    expected /= n
    
    return expected

# Read input
n, c = map(int, input().split())
cards = list(map(int, input().split()))

# Calculate and output the expected score
result = expected_score(n, c, cards)
print("{:.6f}".format(result))
