
def remaining_number_after_algorithm(T, queries):
    result = []
    for n, x in queries:
        result.append(2*x)
    return result

# Input
T = 3
queries = [(3, 1), (4, 2), (69, 6)]

# Output
output = remaining_number_after_algorithm(T, queries)
for val in output:
    print(val)
