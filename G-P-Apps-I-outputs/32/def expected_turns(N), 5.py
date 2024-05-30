
def expected_turns(N):
    total_pairs = 2 * N
    remaining_pairs = total_pairs
    matching_pairs = 0
    turns = 0
    
    while remaining_pairs > 0:
        remaining_pairs -= 2
        matching_pairs += 1
        
        # First card matching
        if matching_pairs > 1:
            turns += 1
        
        # Second card matching
        if matching_pairs > 1:
            turns += 1
        
        # Non-matching case
        turns += 1

    return turns

N = int(input())
expected_turns = expected_turns(N)
print("{:.9f}".format(expected_turns))
```
