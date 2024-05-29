
def last_child(n, m, candies):
    remaining_candies = list(candies)
    positions = list(range(1, n+1))
    current_index = 0

    while len(remaining_candies) > 0:
        if remaining_candies[current_index] <= m:
            remaining_candies.pop(current_index)
            positions.pop(current_index)
        else:
            remaining_candies[current_index] -= m
            positions.append(positions.pop(current_index))

    return positions[-1]

# Input processing
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(last_child(n, m, a))
```
