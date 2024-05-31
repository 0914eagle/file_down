
def calculate_probability_of_self_gifts(N):
    if N == 1:
        return 0.0
    elif N == 2:
        return 0.5
    else:
        probability = 1.0
        for i in range(2, N+1):
            probability *= (i-1) / i
        return round(1 - probability, 8)

# Read input
N = int(input())

# Calculate and print the probability
print("{:.8f}".format(calculate_probability_of_self_gifts(N)))
