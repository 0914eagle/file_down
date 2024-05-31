
def hours_pass_in_world_A(T, X):
    hours_in_world_A = T / X
    return hours_in_world_A

# Read input from Standard Input
T, X = map(int, input().split())

# Calculate and print the result
result = hours_pass_in_world_A(T, X)
print("{:.10f}".format(result))
