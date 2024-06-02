
def count_valid_decks(n, k, cards):
    prefix_products = [1]
    for card in cards:
        prefix_products.append(prefix_products[-1] * card)

    suffix_products = [1]
    for card in reversed(cards):
        suffix_products.append(suffix_products[-1] * card)

    suffix_products = list(reversed(suffix_products))

    count = 0
    for x in range(n + 1):
        for y in range(n + 1):
            if x + y >= n:
                break
            if (prefix_products[x] * suffix_products[n - y]) % k == 0:
                count += 1

    return count

# Input
n, k = map(int, input().split())
cards = list(map(int, input().split()))

# Output
print(count_valid_decks(n, k, cards))
