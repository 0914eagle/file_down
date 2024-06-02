
def make_a_pile(n):
    stones = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stones.append(n + i)
        else:
            stones.append(n + 2*i)
    return stones

# Test the function
print(make_a_pile(3))  # Output: [3, 5, 7]
