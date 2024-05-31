
def expected_score(n, c, cards):
    expected = 0
    for i in range(1, n - c + 2):
        count = 0
        for j in range(i, n):
            if cards[j] > max(cards[i-1:i-1+c]):
                break
            count += 1
        expected += count * cards[i-1]
    return format(expected / (n - c + 1), '.6f')

# Input
n, c = map(int, input().split())
cards = list(map(int, input().split()))

# Output
print(expected_score(n, c, cards))
