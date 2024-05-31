
def expected_score(n, c, cards):
    cards.sort()
    prob = [0] * n
    prob[0] = 1

    for i in range(1, n):
        prob[i] = prob[i-1] * (c-i+1) / (n-i)

    expected = 0
    for i in range(n):
        expected += prob[i] * cards[i]

    return expected

# Input reading and function call
n, c = map(int, input().split())
cards = list(map(int, input().split()))
result = expected_score(n, c, cards)
print("{:.6f}".format(result))
