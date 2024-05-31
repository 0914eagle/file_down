
def count_pyramids(n):
    pyramids = 0
    remaining_cards = n
    
    while remaining_cards >= 2 * (pyramids + 1):
        pyramids += 1
        remaining_cards -= 2 * pyramids

    return pyramids

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_pyramids(n))
