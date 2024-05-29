
def count_frogs(n, d, frogs):
    frogs.sort(key=lambda x: x[1])  # Sort frogs by weight
    pile = []  # Initialize an empty pile of frogs
    escaped_count = 0  # Keep track of the number of frogs that have escaped
    for frog in frogs:
        if frog[0] >= d:  # If a frog can directly escape, increase escaped count and continue
            escaped_count += 1
            continue

        # Try to find a frog in the pile that can carry the current frog
        carry_index = -1
        for i, pile_frog in enumerate(pile):
            if pile_frog[1] >= frog[1]:  # Check weight constraint
                if pile_frog[2] + frog[0] >= d:  # Check height constraint
                    carry_index = i
                    break

        if carry_index != -1:
            pile.pop(carry_index)  # Remove carrying frog from pile
        pile.append(frog)  # Add current frog to pile

    return escaped_count + len(pile)  # Return total number of escaped frogs

# Read input
n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the result
print(count_frogs(n, d, frogs))
```
