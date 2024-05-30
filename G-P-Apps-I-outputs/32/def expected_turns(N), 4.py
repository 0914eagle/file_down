
def expected_turns(N):
    total_cards = 2 * N
    expectation = 0
    known_cards = set()
    
    for i in range(1, total_cards+1):
        remaining_pairs = N - len(known_cards) // 2
        expectation += 2 * remaining_pairs / (total_cards - i + 1)
        known_cards.add(i)
        
    return expectation

N = int(input())
result = expected_turns(N)
print("{:.9f}".format(result))
```
