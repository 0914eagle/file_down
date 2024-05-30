
def expected_turns(N):
    total_cards = 2 * N
    expected_turns = 0
    
    for i in range(1, total_cards + 1):
        expected_turns += 2 * (total_cards - i + 1) / i
        
    return expected_turns

N = int(input().strip())
result = expected_turns(N)
print("{:.9f}".format(result))
```
