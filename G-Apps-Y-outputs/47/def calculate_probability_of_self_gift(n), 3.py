
def calculate_probability_of_self_gift(n):
    if n == 1:
        return 0.0
    elif n == 2:
        return 0.5
    else:
        probability = 1.0
        for i in range(1, n+1):
            probability *= 1 - (i / n)
        return round(1 - probability, 8)

# Read input
N = int(input())

# Calculate and print the probability
print(calculate_probability_of_self_gift(N))
