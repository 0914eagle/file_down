
def count_criminals(n, a, cities):
    criminals_captured = 0

    for i in range(n):
        distance = abs(a - i + 1)
        if cities[i] == 1 and distance > 0:
            criminals_captured += 1

    return criminals_captured

# Read input
n, a = map(int, input().split())
cities = list(map(int, input().split()))

# Call the function
result = count_criminals(n, a, cities)

# Print the result
print(result)
