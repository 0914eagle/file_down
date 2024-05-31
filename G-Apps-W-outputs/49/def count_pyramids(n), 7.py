
def count_pyramids(n):
    pyramid_count = 0
    remaining_cards = n
    
    while remaining_cards >= pyramid_count + 2:
        pyramid_count += 1
        remaining_cards -= pyramid_count + 1
    
    return pyramid_count

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_pyramids(n))
