
def hours_pass_in_world_a(T, X):
    hours_in_world_a = T / X
    return hours_in_world_a

# Read input values
T, X = map(int, input().split())

# Calculate and print the result
result = hours_pass_in_world_a(T, X)
print("{:.10f}".format(result))
