
def hours_passed_in_world_A(T, X):
    return T / X

# Read input from Standard Input
T, X = map(int, input().split())

result = hours_passed_in_world_A(T, X)
print("{:.10f}".format(result))
