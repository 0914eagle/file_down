
def shortest_test_scheme(k, allergens):
    max_duration = max(allergens)
    total_days = max_duration
    return total_days + 1

# Reading input
k = int(input())
allergens = [int(input()) for _ in range(k)]

# Getting the shortest test scheme
shortest_scheme = shortest_test_scheme(k, allergens)
print(shortest_scheme)
