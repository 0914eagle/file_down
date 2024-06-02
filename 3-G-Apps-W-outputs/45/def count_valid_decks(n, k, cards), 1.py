
def count_valid_decks(n, k, cards):
    prefix_product = [1] * (n + 1)
    suffix_product = [1] * (n + 1)
    
    for i in range(1, n + 1):
        prefix_product[i] = prefix_product[i - 1] * cards[i - 1]
    
    for i in range(n, 0, -1):
        suffix_product[i] = suffix_product[i + 1] * cards[i - 1]
    
    count = 0
    for x in range(n + 1):
        for y in range(n + 1):
            if x + y >= n:
                break
            if (prefix_product[x] * suffix_product[n - y + 1]) % k == 0:
                count += 1
    
    return count

# Input
n, k = map(int, input().split())
cards = list(map(int, input().split()))

# Output
print(count_valid_decks(n, k, cards))
